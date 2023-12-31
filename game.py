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
        squig_0 = (0x44, 0xAA, 0x10)
        squig_1 = (0x88, 0x54, 0x22)
        squig_2 = (0x10, 0xAA, 0x44)
        squig_3 = (0x22, 0x54, 0x88)
        p_0 = (0x04, 0xFC, 0x04)
        p_1 = (0x10, 0xFC, 0x10)
        p_2 = (0x20, 0xFC, 0x20)
        p_3 = (0x80, 0xFC, 0x80)
        r0 = (0x00, 0xFE, 0x00)
        r1 = (0x24, 0xFE, 0x12)
        r2 = (0x00, 0xFE, 0x00)
        r3 = (0x48, 0xFE, 0x90)
        # shield is 22 pixels by 16 pixels, 44 bytes
        shield = (
            0xFF, 0x0F, 0xFF, 0x1F, 0xFF, 0x3F, 0xFF, 0x7F, 0xFF, 0xFF, 0xFC,
            0xFF, 0xF8, 0xFF, 0xF0, 0xFF, 0xF0, 0xFF, 0xF0, 0xFF, 0xF0, 0xFF,
            0xF0, 0xFF, 0xF0, 0xFF, 0xF0, 0xFF, 0xF8, 0xFF, 0xFC, 0xFF, 0xFF,
            0xFF, 0xFF, 0xFF, 0xFF, 0x7F, 0xFF, 0x3F, 0xFF, 0x1F, 0xFF, 0x0F)
        if not testing:
            pygame.init()
            pygame.display.set_caption("Space Invaders")
            self.delta_time = 0
            self.clock = pygame.time.Clock()
            self.screen = pygame.display.set_mode((512, 768))
            aliens = (alien10, alien11, alien20, alien21, alien30, alien31)
            self.aliens = [self.make_and_scale_surface(bytes, 8) for bytes in aliens]
            players = (player, player_e0, player_e1)
            self.players = [self.make_and_scale_surface(bytes, 8) for bytes in players]
            saucers = (saucer, saucer_e)
            self.saucers = [self.make_and_scale_surface(saucer, 8, (24, 8)) for saucer in saucers]
            self.saucer = self.make_and_scale_surface(saucer, 8, (24, 8))
            self.squig = self.make_and_scale_surface(squig_0, 8, (3, 8))
            squigs = (squig_0, squig_1, squig_2, squig_3)
            self.squigs = [self.make_and_scale_surface(squig, 8, (3, 8)) for squig in squigs]
            plungers = (p_0, p_1, p_2, p_3)
            self.plungers = [self.make_and_scale_surface(plunger, 8, (3, 8)) for plunger in plungers]
            rollers = (r0, r1, r2, r3)
            self.rollers = [self.make_and_scale_surface(plunger, 8, (3, 8)) for plunger in rollers]
            self.shield = self.make_and_scale_surface(shield, 8, (22, 16))
        self.player_location = Vector2(128, 128)

    def make_and_scale_surface(self, bytes, scale, size=(16, 8)):
        return pygame.transform.scale_by(self.make_surface(bytes, size), scale)

    def make_surface(self, bytes, size=(16, 8)):
        s = Surface(size)
        s.set_colorkey((0, 0, 0))
        width = size[0]
        layers = len(bytes)//width
        for x, byte in enumerate(bytes):
            x_in = x // layers
            y_offset = 0 if layers == 1 else 8 - (x % layers)*8
            self.store_byte(byte, x_in, y_offset, s)
        return s

    def store_byte(self, byte, x, y_offset, surface):
        for z in range(8):
            bit = byte & 1
            y = y_offset + 7 - z
            if bit:
                surface.set_at((x, y), "white")
            byte = byte >> 1

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
            # dest = (32, 512)
            # self.screen.blit(self.squig, dest)
            for s, squiggle in enumerate(self.squigs):
                dest = (32 + 36*s, 512)
                self.screen.blit(squiggle, dest)
            for s, plunger in enumerate(self.plungers):
                dest = (32 + 160 + 36*s, 512)
                self.screen.blit(plunger, dest)
            for s, roller in enumerate(self.rollers):
                dest = (32 + 320 + 36*s, 512)
                self.screen.blit(roller, dest)
            dest = (32, 512 + 80)
            self.screen.blit(self.shield, dest)
            pygame.display.flip()
            self.delta_time = self.clock.tick(60) / 1000
        return "done"
