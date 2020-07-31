import pygame
import os
import time
from Goblin import Goblin
from Beast import Beast
from Boss import Boss
from ArcherTower import ArcherTower, ArcherTowerShort
from SupportTower import DamageTower, RangeTower
import random
from Menu import MainMenu

pygame.font.init()

attackTowerNames = ['short', 'long']
supportTowerNames = ['range', 'damage']
class Game:
    def __init__(self):
        self.width = 1100
        self.height = 700
        self.window = pygame.display.set_mode((self.width, self.height))
        self.enemies=[]
        #ArcherTower(100, 580), , ArcherTower(900, 164)
        self.attackTowers=[ ArcherTower(488, 170)]
        self.supportTowers = [RangeTower(533, 164), DamageTower(452, 237)]
        self.lives=10
        self.score = 1000
        self.bg = pygame.image.load(os.path.join("background", "bg.png"))
        self.timer = time.time()

        self.heart = pygame.image.load(os.path.join("assets", "heart.png"))
        self.jewel = pygame.image.load(os.path.join("assets", "jewel.png"))
        self.text = pygame.font.Font('freesansbold.ttf', 40)
        self.menu = MainMenu(0, 85)

        #used to check if a new tower is being created
        self.isNewTower = False
        self.newTower = None
        self.newTowerType = ''



    def displayTitle(self):
        pygame.display.set_caption("Tower Defense")

    #displays heart icon and number of lives onto screen
    def displayLives(self):
        # transform the heart icon to 32 x 32
        self.heart = pygame.transform.scale(self.heart, (32, 32))
        # blit onto the screen
        self.window.blit(self.heart, (15, 10))

        font = self.text.render( str(self.lives), True, (255, 255, 255))

        self.window.blit(font, (self.heart.get_width() + 20, 10 ))


    def displayScore(self):
        #transform the jewel icon to 32 x 32
        self.jewel = pygame.transform.scale(self.jewel, (32,32))
        #blit onto the screen
        self.window.blit(self.jewel, (15, 50))

        font = self.text.render( str(self.score), True, (255,255,255))
        self.window.blit(font, (self.jewel.get_width() + 20, 50))


    # adds new Tower object and displays based on your mouse position
    def addTower(self, name):
        x, y = pygame.mouse.get_pos()
        towerName = ['short', 'long', 'range', 'damage']
        towers = [ArcherTowerShort(x,y), ArcherTower(x,y) , RangeTower(x,y), DamageTower(x,y)]

        try:
            obj = towers[towerName.index(name)]
            self.newTower = obj

        except Exception as e:
            print(str(e) + 'Not Valid Name')



    def drawWindow(self):
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.window.blit(self.bg, (0, 0))

        #draw menu on screen
        self.menu.drawMenu(self.window)

        #displays how many lives you have
        self.displayLives()

        #displays your current score
        self.displayScore()

        #draw all the enemies in the list onto the window
        for enemy in self.enemies:
            enemy.drawEnemy(self.window)

        #draw attack towers
        for tower in self.attackTowers:
            tower.drawTower(self.window)

        #draw support towers
        for tower in self.supportTowers:
            tower.drawTower(self.window)

        # if the newTower boolean is set to true draw that object on the screen
        if self.isNewTower:
            #need to call add Tower so the tower is being displayed on the window
            self.addTower(self.newTowerType)
            self.newTower.drawTower(self.window)

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
                    #print(pos)

                    # check to see if the condition for new tower creation is set to true
                    if self.isNewTower:
                        if self.newTowerType in attackTowerNames:
                            self.attackTowers.append(self.newTower)
                        elif self.newTowerType in supportTowerNames:
                            self.supportTowers.append(self.newTower)

                        self.isNewTower = False
                        self.newTowerType = ''

                    # check if any of the menu buttons are clicked
                    for button in self.menu.buttons:
                        if button.buttonClicked(pos[0], pos[1]):
                            if button.get_buttonType() == 'short' and self.score >= 500:
                                self.score -= 500
                                self.isNewTower = True
                                self.newTowerType = 'short'
                                self.addTower(self.newTowerType)
                            elif button.get_buttonType() == 'long' and self.score >= 750:
                                self.score -= 750
                                self.isNewTower = True
                                self.newTowerType = 'long'
                                self.addTower(self.newTowerType)
                            elif button.get_buttonType() == 'range' and self.score >= 1000:
                                self.score -= 1000
                                self.isNewTower = True
                                self.newTowerType = 'range'
                                self.addTower(self.newTowerType)
                            elif button.get_buttonType() == 'damage' and self.score >= 1000:
                                self.score -= 1000
                                self.isNewTower = True
                                self.newTowerType = 'damage'
                                self.addTower(self.newTowerType)



                    #check to see if any of the attack towers or support towers  were clicked
                    for tower in self.attackTowers:
                        #returns an int based on whether or not the upgrade button was clicked, if so deduct it from the players score
                        upgrade_cost = tower.click(pos[0], pos[1], self.score)
                        self.score -= upgrade_cost

                    #check to see if any of the supporttowers were clicked
                    for tower in self.supportTowers:
                        # returns an int based on whether or not the upgrade button was clicked, if so deduct it from the players score
                        upgrade_cost = tower.click(pos[0], pos[1], self.score)
                        self.score -= upgrade_cost


            #loops through the enemies and check their position
            for enemy in self.enemies:
                if enemy.pos_y > 700:
                    self.enemies.remove(enemy)

                    #remove a life if the enemy makes it through the whole path based on the damage property in enemy class
                    self.lives -= enemy.damage

            #loop through attack towers and performs attack method
            for tower in self.attackTowers:
                # tower attack returns an int based on whether or not an enemy is killed, add this to the score
                add_score = tower.attack(self.enemies)
                self.score += add_score


            for tower in self.supportTowers:
                # performs support method
                tower.support(self.attackTowers)


            self.drawWindow()




game = Game()
game.run()
