import pygame
import os
import time
from Goblin import Goblin
from Beast import Beast
from Boss import Boss
from ArcherTower import ArcherTower
import random

pygame.font.init()

class Game:
    def __init__(self):
        self.width = 1100
        self.height = 700
        self.window = pygame.display.set_mode((self.width, self.height))
        self.enemies=[]
        self.towers=[ArcherTower(100, 580), ArcherTower(488, 170), ArcherTower(900, 164)]
        self.lives=10
        self.bg = pygame.image.load(os.path.join("background", "bg.png"))
        self.timer = time.time()
        self.heart = pygame.image.load(os.path.join("assets", "heart.png"))
        self.text = pygame.font.Font('freesansbold.ttf', 40)


    def displayTitle(self):
        pygame.display.set_caption("Tower Defense")

    #displays heart icon and number of lives onto screen
    def displayLives(self):
        # transform the heart icon to 32 x 32
        self.heart = pygame.transform.scale(self.heart, (32, 32))
        # blit onto the screen
        self.window.blit(self.heart, (self.width - 42, 10))

        font = self.text.render( 'x' + str(self.lives), True, (255, 255, 255))

        self.window.blit(font, (self.width - 115, 10 ))


    def drawWindow(self):
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.window.blit(self.bg, (0, 0))

        self.displayLives()

        #draw all the enemies in the list onto the window
        for enemy in self.enemies:
            enemy.drawEnemy(self.window)

        #draw towers
        for tower in self.towers:
            tower.drawTower(self.window)

        pygame.display.update()


    def run(self):
        run = True
        clock = pygame.time.Clock()
        pygame.init()
        self.displayTitle()

        while run:
            if time.time() - self.timer > 1:
                self.timer = time.time()
                self.enemies.append(random.choice([Goblin(), Beast(), Boss()]))
            clock.tick(30)
            #pygame.time.delay(200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for tower in self.towers:
                        tower.click(pos[0], pos[1])


            #loops through the enemies and check their position
            for enemy in self.enemies:
                if enemy.pos_y > 700:
                    self.enemies.remove(enemy)

            for tower in self.towers:
                tower.attack(self.enemies)


            self.drawWindow()




game = Game()
game.run()
