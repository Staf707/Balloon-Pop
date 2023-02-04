from const import *
from player import Player
import pygame

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.players = [Player(surface)]
    def gameloop(self):
        for player in self.players:
            player._player()
            if player.position[1] < -PLAYER_SCALE:
                self.players.remove(player)
    
    def shoot(self):
        self.players[-1].speed_y = -self.players[-1].max_speed
        self.players[-1].has_shot = True
    
    def new_player(self):
        self.players.append(Player(self.surface))
