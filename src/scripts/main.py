from const import *
import pygame, sys
from game import Game

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

        self.bg = pygame.image.load(self.path)

    def loop(self):

        clock = pygame.time.Clock()
        pygame.init()
        while True:
            self.path = 'src/graphics/background/background' + str(self.bg_count) + '.png'

            self.bg = pygame.image.load(self.path)
            self.screen.blit(self.bg, (0,0))
            pygame.display.set_caption("Balloon Pop")
            self.game.gameloop()
            # shoot waiting
            if self.can_shoot == False:

                self.cur_time += 0.5
                if self.cur_time >= 15:
                    self.can_shoot = True
                    self.cur_time = 0
            # bg animating
            self.bg_cur_time += 1
            if self.bg_cur_time >= 15:
                
                if self.bg_count <= 39:
                    self.bg_count += 1
                else: self.bg_count = 1
                self.bg_cur_time = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.can_shoot:
                    self.game.shoot()
                    
                    self.game.new_player()
                    self.can_shoot = False
            # game loop    

            # update and fps      
            clock.tick(FPS)
            pygame.display.update()

main = Main()
if __name__ == "__main__":
    main.loop()