# Invaders Game
import pygame as pygame
from pygame import Rect, KEYDOWN, K_ESCAPE, QUIT, Vector2, Surface, Color


class Game:
    def __init__(self, testing=False):
        self._testing = testing
        alien10 = (0x00, 0x00, 0x39, 0x79, 0x7A, 0x6E, 0xEC, 0xFA, 0xFA, 0xEC, 0x6E, 0x7A, 0x79, 0x39, 0x00, 0x00)
        alien20 = (0x00, 0x00, 0x00, 0x78, 0x1D, 0xBE, 0x6C, 0x3C, 0x3C, 0x3C, 0x6C, 0xBE, 0x1D, 0x78, 0x00, 0x00)
        alien30 = (0x00, 0x00, 0x00, 0x00, 0x19, 0x3A, 0x6D, 0xFA, 0xFA, 0x6D, 0x3A, 0x19, 0x00, 0x00, 0x00, 0x00)
        alien11 = (0x00, 0x00, 0x38, 0x7A, 0x7F, 0x6D, 0xEC, 0xFA, 0xFA, 0xEC, 0x6D, 0x7F, 0x7A, 0x38, 0x00, 0x00)
        alien21 = (0x00, 0x00, 0x00, 0x0E, 0x18, 0xBE, 0x6D, 0x3D, 0x3C, 0x3D, 0x6D, 0xBE, 0x18, 0x0E, 0x00, 0x00)
        alien31 = (0x00, 0x00, 0x00, 0x00, 0x1A, 0x3D, 0x68, 0xFC, 0xFC, 0x68, 0x3D, 0x1A, 0x00, 0x00, 0x00, 0x00)
        player = (0x00, 0x00, 0x0F, 0x1F, 0x1F, 0x1F, 0x1F, 0x7F, 0xFF, 0x7F, 0x1F, 0x1F, 0x1F, 0x1F, 0x0F, 0x00)
        player_e0 = (0x00, 0x04, 0x01, 0x13, 0x03, 0x07, 0xB3, 0x0F, 0x2F, 0x03, 0x2F, 0x49, 0x04, 0x03, 0x00, 0x01)
        player_e1 = (0x40, 0x08, 0x05, 0xA3, 0x0A, 0x03, 0x5B, 0x0F, 0x27, 0x27, 0x0B, 0x4B, 0x40, 0x84, 0x11, 0x48)
        saucer = (0x00, 0x00, 0x00, 0x00, 0x04, 0x0C, 0x1E, 0x37, 0x3E, 0x7C, 0x74, 0x7E, 0x7E, 0x74, 0x7C, 0x3E, 0x37,
                  0x1E, 0x0C, 0x04, 0x00, 0x00, 0x00, 0x00)
        saucer_e = (0x00, 0x22, 0x00, 0xA5, 0x40, 0x08, 0x98, 0x3D, 0xB6, 0x3C, 0x36, 0x1D, 0x10, 0x48, 0x62, 0xB6,
                    0x1D, 0x98, 0x08, 0x42, 0x90, 0x08, 0x00, 0x00)
        if not testing:
            pygame.init()
            pygame.display.set_caption("Space Invaders")
            self.delta_time = 0
            self.clock = pygame.time.Clock()
            self.screen = pygame.display.set_mode((512, 768))
            # self.alien10 = self.alien_surface(alien10)
            # self.alien20 = self.alien_surface(alien20)
            # self.alien30 = self.alien_surface(alien30)
            # self.alien10 = pygame.transform.scale_by(self.alien10, 4)
            # self.alien20 = pygame.transform.scale_by(self.alien20, 4)
            # self.alien30 = pygame.transform.scale_by(self.alien30, 4)
            # self.alien11 = pygame.transform.scale_by(self.alien_surface(alien11), 4)
            # self.alien21 = pygame.transform.scale_by(self.alien_surface(alien21), 4)
            # self.alien31 = self.make_alien(alien31, 4)
            aliens = (alien10, alien11, alien20, alien21, alien30, alien31)
            self.aliens = [self.make_and_scale_surface(bytes, 8) for bytes in aliens]
            players = (player, player_e0, player_e1)
            self.players = [self.make_and_scale_surface(bytes, 8) for bytes in players]
            saucers = (saucer, saucer_e)
            self.saucers = [self.make_and_scale_surface(saucer, 8, (24, 8)) for saucer in saucers]
            self.saucer = self.make_and_scale_surface(saucer, 8, (24, 8))
        self.player_location = Vector2(128, 128)

    def make_and_scale_surface(self, bytes, scale, size=(16, 8)):
        return pygame.transform.scale_by(self.make_surface(bytes, size), scale)

    def make_surface(self, alien, size=(16, 8)):
        s = Surface(size)
        s.set_colorkey((0, 0, 0))
        count = 0
        for byte in alien:
            for z in range(8):
                bit = byte & 1
                x, y = divmod(count, 8)
                if bit:
                    s.set_at((x, 7-y), "white")
                byte = byte >> 1
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
            for i, alien in enumerate(self.aliens):
                #  0   1   2   3   4   5
                # 10, 11, 20, 21, 30, 31
                x_base = 32
                x_off = 256*(i%2)
                dest = (x_base + x_off, 16+80*(i//2))
                self.screen.blit(alien, dest)
            for p, player in enumerate(self.players):
                dest = (32, 256 + 80*p)
                self.screen.blit(player, dest)
            for s, saucer in enumerate(self.saucers):
                dest = (32+256, 256 + 80*s)
                self.screen.blit(saucer, dest)
            pygame.display.flip()
            self.delta_time = self.clock.tick(60) / 1000
        return "done"
