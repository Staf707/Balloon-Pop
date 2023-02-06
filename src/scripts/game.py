from const import *
from player import Player
from balloon import Balloon
from hearth import Hearth
import random
import pygame

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.balloon_count = 5
        self.level = 1
        self.av_speed = 2
        self.players = [Player(surface)]
        self.balloons = []
        self.hearths = []
        self.level_loaded = False
        self.game_over = False
        self.lives = 3
    def gameloop(self):
        for player in self.players:
            player._player()
            if player.position[1] < -PLAYER_SCALE:
                self.players.remove(player)
        for i, balloon in enumerate(self.balloons):
            balloon.draw_balloon()
            balloon.move_balloon()
            for player in self.players:
                if player.player.get_rect(topleft = (player.position[0], player.position[1])).colliderect(balloon.img.get_rect(topleft = (balloon.x_position, balloon.random_y_pos))):
                    self.balloons.pop(i)
        
        if len(self.balloons) <= self.balloon_count - 1 and self.level_loaded == False:
            self.balloons.append(Balloon(self.surface, random.uniform(self.av_speed - 1, self.av_speed + 2)))
        else:
            self.level_loaded = True
        if len(self.balloons) == 0:
            self.level_up()
        for hearth in self.hearths:
            hearth.draw_hearths()
        self.check_game_over()
    def shoot(self):
        self.players[-1].speed_y = -self.players[-1].max_speed
        self.players[-1].has_shot = True


    def new_player(self):
        self.players.append(Player(self.surface))


    def level_up(self):
        self.level_loaded = False
        self.level += 1
        self.av_speed += 0.5
        self.balloon_count += 5
    def add_hearths(self):

        self.hearths.append(Hearth(self.surface,1))
        self.hearths.append(Hearth(self.surface,2))
        self.hearths.append(Hearth(self.surface,3))
    def check_game_over(self):
        
        if not self.game_over:
            for balloon in self.balloons:
                if balloon.x_position >= WIDTH:
                    self.lives -= 1
                    self.balloons.remove(balloon)
            if self.lives == 0:
                self.game_over = True