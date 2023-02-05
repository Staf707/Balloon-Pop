from const import *
from player import Player
from balloon import Balloon
import pygame

class Game:
    def __init__(self, surface):
        self.surface = surface

        self.players = [Player(surface)]
        self.balloons = []
    def gameloop(self):
        for player in self.players:
            player._player()
            if player.position[1] < -PLAYER_SCALE:
                self.players.remove(player)
    
    def shoot(self):
        self.players[-1].speed_y = -self.players[-1].max_speed
        self.players[-1].has_shot = True
        self.spawn_new_balloon(5)
    def new_player(self):
        self.players.append(Player(self.surface))

    def spawn_new_balloon(self, speed):
        # spawn new balloon with parameter speed
        self.balloons.append(Balloon(self.surface, speed))
