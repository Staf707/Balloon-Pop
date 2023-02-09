from const import *
import pygame, sys
from game import Game
pygame.font.init()
pygame.mixer.init()
class Main:
    def __init__(self):
        self.height = HEIGHT
        self.width = WIDTH
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.game = Game(self.screen)
        self.cur_time = 0
        self.bg_cur_time = 0
        self.can_shoot = True
        self.bg_count = 1
        self.path = 'src/graphics/background/background' + str(self.bg_count) + '.png'
        self.song = 1 
        self.music_path = "src/graphics/music/music" + str(self.song) + ".wav"
        self.bg = pygame.image.load(self.path)
        self.paused = False
        self.song_played = False
    def loop(self):

        clock = pygame.time.Clock()
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.5)
        pygame.init()
        while True:
            self.path = 'src/graphics/background/background' + str(self.bg_count) + '.png'

            self.bg = pygame.image.load(self.path)
            self.screen.blit(self.bg, (0,0))
            pygame.display.set_caption("Balloon Pop")
            self.game.gameloop(self.paused)
            # shoot delaying
            if self.can_shoot == False and not self.paused:

                self.cur_time += 0.5
                if self.cur_time >= 15:
                    self.can_shoot = True
                    self.cur_time = 0
            # bg animating
            self.bg_cur_time += 1
            if self.bg_cur_time >= 10:
                
                if self.bg_count <= 39:
                    self.bg_count += 1
                else: self.bg_count = 1
                self.bg_cur_time = 0
            if self.game.game_over and not self.song_played:
                self.music_path = "src/graphics/music/game_over_music.wav"
                pygame.mixer.music.load(self.music_path)
                pygame.mixer.music.play(-1, 0.0)
                self.song_played = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.can_shoot and not self.paused:
                    self.game.shoot()
                    
                    self.game.new_player()
                    self.can_shoot = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4 and not self.game.game_over: self.next_song()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5 and not self.game.game_over: self.previous_song()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.game.play_button.get_rect(topleft=(WIDTH- 160, 45)).collidepoint(x, y) and not self.game.game_over: self.previous_song()
                    elif self.game.back_button.get_rect(topleft=(WIDTH- 100, 45)).collidepoint(x, y) and not self.game.game_over: self.next_song()
                    if event.button == 1 and self.game.play_again_button.get_rect(topleft=(WIDTH / 2 - self.game.play_again_button.get_width() / 2,HEIGHT / 2 - self.game.play_again_button.get_height() / 2)).collidepoint(x, y) and self.game.game_over: 
                        self.game.reset_game()
                        self.music_path = "src/graphics/music/music" + str(self.song) + ".wav"
                        self.song_played = False
                        pygame.mixer.music.load(self.music_path)
                        pygame.mixer.music.play(-1, 0.0)
                        pygame.mixer.music.set_volume(0.5)
                # check escape key
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused
                        if self.paused: pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
            # game loop    

            # update and fps      
            clock.tick(FPS)
            pygame.display.update()
    
    def next_song(self):
        if self.song == 6:
            self.song = 0



        self.song += 1
        self.music_path = "src/graphics/music/music" + str(self.song) + ".wav"
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1, 0.0)
    def previous_song(self):
        if self.song == 1:
            self.song = 6
            
        else:
            self.song -= 1
        self.music_path = "src/graphics/music/music" + str(self.song) + ".wav"
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1, 0.0)
main = Main()
if __name__ == "__main__":
    main.loop()