import pygame
import os

class Game:
    def __init__(self):
        self.width = 1100
        self.height = 700
        self.window = pygame.display.set_mode((self.width, self.height))
        self.enemies=[]
        self.towers=[]
        self.lives=10
        self.bg = pygame.image.load(os.path.join("background", "bg.png"))

    def displayTitle(self):
        pygame.display.set_caption("Tower Defense")



    def displayBg(self):
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.window.blit(self.bg, (0,0))

    def run(self):
        run = True
        pygame.init()
        self.displayBg()
        self.displayTitle()

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

game = Game()
game.run()
