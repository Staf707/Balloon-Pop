from const import *
import pygame
import random

class Balloon:
    def __init__(self, surface,speed):
        self.surface = surface
        self.speed = speed
        self.scale = BALLOON_SCALE
        self.frame = 1
        self.balloon_time = 0
        self.color = str(random.choice(COLORS))
        self.path = "src/graphics/balloons/" + self.color + "/balloon_" + self.color + str(self.frame) + ".png"
        self.img = pygame.transform.scale(pygame.image.load(self.path), (self.scale / 2, self.scale))
        self.random_y_pos = random.randint(100, HEIGHT - 200)
        self.x_position = random.randint(-500, -300)

    def draw_balloon(self):
        # DRAW BALLOON

        # update balloon animation
        self.path = "src/graphics/balloons/" + self.color + "/balloon_" + self.color + str(self.frame) + ".png"       
        self.img = pygame.transform.scale(pygame.image.load(self.path), (self.scale / 2, self.scale))
        
        self.balloon_time += 1
        if self.balloon_time >= 10:
                
            if self.frame <= 14:
                self.frame += 1
            else: self.frame = 1
            self.balloon_time = 0
        self.surface.blit(self.img, (self.x_position,self.random_y_pos))
    
    def move_balloon(self):
        self.x_position += self.speed