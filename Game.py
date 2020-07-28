import pygame
import os
import time
from Goblin import Goblin
from Beast import Beast
from Gremlin import Gremlin
from ArcherTower import ArcherTower

class Game:
    def __init__(self):
        self.width = 1100
        self.height = 700
        self.window = pygame.display.set_mode((self.width, self.height))
        self.enemies=[Gremlin()]
        self.towers=[ArcherTower(100, 580)]
        self.lives=10
        self.bg = pygame.image.load(os.path.join("background", "bg.png"))


    def displayTitle(self):
        pygame.display.set_caption("Tower Defense")

    def drawWindow(self):
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.window.blit(self.bg, (0, 0))

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
            clock.tick(30)
            #pygame.time.delay(200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False



            #to_delete=[]

            #loops through the enemies and check their position
            for enemy in self.enemies:
                if enemy.pos_y > 700:
                    self.enemies.remove(enemy)

            for tower in self.towers:
                tower.attack(self.enemies)

            #delete the enemy fromt eh array
            #for d in to_delete:
             #   self.enemies.remove(d)


            self.drawWindow()




game = Game()
game.run()
