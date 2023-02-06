import pygame
from const import *
class Hearth:
    def __init__(self, surface):
        self.surface = surface
        self.scale = HEARTH_SCALE
        self.hearth_img = pygame.transform.scale(pygame.image.load("src/graphics/ui/hearth.png"),(self.scale,self.scale))
        self.empty_hearth_img = pygame.transform.scale(pygame.image.load("src/graphics/ui/broken_hearth.png"),(self.scale,self.scale))
    def h3(self):
        self.surface.blit(self.hearth_img, (WIDTH / 2 - self.scale / 2,20))
        self.surface.blit(self.hearth_img, (WIDTH / 2 - self.scale - 40,20))
        self.surface.blit(self.hearth_img, (WIDTH / 2 + 40,20))
    def h2(self):
        self.surface.blit(self.hearth_img, (WIDTH / 2 - self.scale - 40,20))
        self.surface.blit(self.hearth_img, (WIDTH / 2 - self.scale / 2,20))
        self.surface.blit(self.empty_hearth_img, (WIDTH / 2 + 40,20))

    def h1(self):
        self.surface.blit(self.hearth_img, (WIDTH / 2 - self.scale - 40,20))
        self.surface.blit(self.empty_hearth_img, (WIDTH / 2 - self.scale / 2,20))
        self.surface.blit(self.empty_hearth_img, (WIDTH / 2 + 40,20))
    
    def h0(self):
        self.surface.blit(self.empty_hearth_img, (WIDTH / 2 - self.scale - 40,20))
        self.surface.blit(self.empty_hearth_img, (WIDTH / 2 - self.scale / 2,20))
        self.surface.blit(self.empty_hearth_img, (WIDTH / 2 + 40,20))