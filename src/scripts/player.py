import pygame
from const import *
from pygame.locals import *
class Player:
    def __init__(self, surface):
        self.scale = PLAYER_SCALE
        self.player = pygame.transform.scale(pygame.image.load("src/graphics/ui/player.png"), (self.scale / 3, self.scale))
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.position = [self.mouse_x - self.scale // 2, HEIGHT - 100]
        self.surface = surface
        self.has_shot = False
        self.max_speed = 15    
        self.speed_y = 0


    def move_player(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        if self.has_shot == False:
            self.position[0] = self.mouse_x
        self.position[1] += self.speed_y
    def draw_player(self):
        self.surface.blit(self.player, (self.position[0], self.position[1]))
