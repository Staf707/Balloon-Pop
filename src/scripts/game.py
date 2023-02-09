from const import *
from player import Player
from balloon import Balloon
from hearth import Hearth
import random
import pygame

class Game:
    def __init__(self, surface):
        self.game_font = pygame.font.Font("src/graphics/fonts/minecraft.ttf", 50)
        self.game_font_small = pygame.font.Font("src/graphics/fonts/minecraft.ttf", 25)
        self.back_button = pygame.image.load("src/graphics/ui/back_button.png")
        self.play_button = pygame.image.load("src/graphics/ui/play_button.png") 
        self.play_again_button = pygame.image.load("src/graphics/ui/play_again.png")
        self.surface = surface
        self.balloon_count = 4
        self.level = 1
        self.av_speed = 2
        self.players = [Player(surface)]
        self.balloons = []
        self.hearth = Hearth(surface)
        self.level_loaded = False
        self.game_over = False
        self.lives = 3
        self.game_started = False
    def gameloop(self, paused):
        for player in self.players:
            if not paused:
                player.move_player()
            player.draw_player()
            if player.position[1] < -PLAYER_SCALE:
                self.players.remove(player)
        for i, balloon in enumerate(self.balloons):
            balloon.draw_balloon()
            if not paused:
                balloon.move_balloon()
            for player in self.players:
                if player.player.get_rect(topleft = (player.position[0], player.position[1])).colliderect(balloon.img.get_rect(topleft = (balloon.x_position, balloon.random_y_pos))):
                    self.balloons.pop(i)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("src/graphics/sound_effects/balloon.wav"))
        
        if len(self.balloons) <= self.balloon_count - 1 and self.level_loaded == False:
            self.balloons.append(Balloon(self.surface, random.uniform(self.av_speed - 1, self.av_speed + 2)))
        else:
            self.level_loaded = True
        if len(self.balloons) == 0 and self.game_over == False:
            self.level_up()
        if paused:
            self.surface.blit(pygame.image.load("src/graphics/ui/pause.png"), (0,0))
            self.draw_paused()
        self.draw_hearths()
        self.check_game_over()
        self.show_level()
    

    def draw_paused(self):
        # draw text
        pause_text = self.game_font.render('GAME PAUSED', False, WHITE)
        self.surface.blit(pause_text, (WIDTH / 2 - pause_text.get_width() / 2,HEIGHT / 2 - pause_text.get_height() / 2))
        # draw music thing
        self.surface.blit(pygame.image.load("src/graphics/ui/box.png"), (WIDTH - 180, 20))
        self.surface.blit(self.back_button, (WIDTH- 160, 45))
        self.surface.blit(self.play_button, (WIDTH- 100, 45))
        # stop music
    def shoot(self):
        if not self.game_over:
            self.players[-1].speed_y = -self.players[-1].max_speed
            self.players[-1].has_shot = True
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("src/graphics/sound_effects/shoot.wav"))


    def show_level(self):
        lvl_over_text = self.game_font_small.render('LEVEL: ' + str(self.level), False, WHITE)
        self.surface.blit(lvl_over_text, (20,20))

    def draw_hearths(self):

        if self.lives == 3:
            self.hearth.h3()
        elif self.lives == 2:
            self.hearth.h2()
        elif self.lives == 1:
            self.hearth.h1()
        elif self.lives == 0:
            self.hearth.h0()
    def new_player(self):
        self.players.append(Player(self.surface))

 
    def level_up(self):
        self.level_loaded = False
        self.level += 1
        self.av_speed += 0.15
        self.balloon_count += 2



    def check_game_over(self):
        
        if not self.game_over:
            for balloon in self.balloons:
                if balloon.x_position >= WIDTH:
                    self.lives -= 1
                    self.balloons.remove(balloon)
            if self.lives == 0:
                self.game_over = True
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("src/graphics/sound_effects/game_over.wav"))

        else: 
            # GAME OVER

            # 1. delete all the balloons
            self.balloons.clear()

            # 2. show game over text
            game_over_text = self.game_font.render('GAME OVER', True, WHITE)
            self.surface.blit(game_over_text, (WIDTH / 2 - game_over_text.get_width() / 2,75))

            # 3. show play again button 

            self.surface.blit(self.play_again_button, (WIDTH / 2 - self.play_again_button.get_width() / 2,HEIGHT / 2 - self.play_again_button.get_height() / 2))
    
    def reset_game(self):
        # 1. clear balloon list
        self.balloon_count = 4
        # change level 
        self.level = 0
        self.av_speed = 2
        self.balloons.clear()
        # 2. change game status
        self.game_over = False
        self.lives = 3
