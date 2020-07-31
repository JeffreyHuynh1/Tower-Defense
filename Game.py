import pygame
import os
import time
from Goblin import Goblin
from Beast import Beast
from Boss import Boss
from ArcherTower import ArcherTower, ArcherTowerShort
from SupportTower import DamageTower, RangeTower
from Button import PlayPauseButton
import random
from Menu import MainMenu
from numpy.random import choice

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
        self.wave = 1
        self.waveSpawnCounter= self.wave * 5
        self.timer = time.time()

        self.bg = pygame.image.load(os.path.join("background", "bg.png"))
        self.waveImage = pygame.transform.scale(pygame.image.load(os.path.join("assets", "wave.png")), (190, 50))
        self.heart = pygame.image.load(os.path.join("assets", "heart.png"))
        self.jewel = pygame.image.load(os.path.join("assets", "jewel.png"))
        self.text = pygame.font.Font('freesansbold.ttf', 40)
        self.menu = MainMenu(0, 85)

        self.playImage = pygame.transform.scale(pygame.image.load(os.path.join("assets", "start.png")) , (64,64))
        self.pauseImage = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pause.png")) , (64,64))
        self.playPauseButton = PlayPauseButton(self.width - self.playImage.get_width() - 10, 10, self.playImage, self.pauseImage)
        self.pause = True

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

    #displays the round
    def displayWave(self):
        self.window.blit(self.waveImage, (0, self.height - self.waveImage.get_height() - 5))
        text = self.text.render('Wave ' + str(self.wave), True, (255,255,255))
        self.window.blit(text, (15, self.height - self.waveImage.get_height() + 5))

    def generateWave(self):
        waveEnemies = [Goblin(), Beast(), Boss()]

        #only spawn enemies if wave spawn counter is greater than 0, keeps track of how many enemies we need to generate
        if self.waveSpawnCounter > 0:
            randEnemy = choice(waveEnemies, 1, p=[.5,.3,.2])
            # append enemy object into our list of enemies
            self.enemies.append(randEnemy[0])
            #decrement the count
            self.waveSpawnCounter -= 1

        # if there are no more enemies to be spawned
        if self.waveSpawnCounter == 0:
            #make sure that there are no enemies in the list, meaning that round is over
            if len(self.enemies) == 0:
                self.wave +=1
                self.waveSpawnCounter = self.wave * 5
                #set pause back to true
                self.pause = True
                #change the image 
                self.playPauseButton.changeImage()


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

        #draw the wave number on screen
        self.displayWave()

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

        # draw play pause button
        self.playPauseButton.drawButton(self.window)

        pygame.display.update()


    def run(self):
        run = True
        clock = pygame.time.Clock()
        pygame.init()
        self.displayTitle()

        while run:
            clock.tick(30)

            if self.pause == False:
                if time.time() - self.timer > 1:
                    self.timer = time.time()
                    self.generateWave()



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

                    #check to see if play or pause button is clciked
                    if self.playPauseButton.buttonClicked(pos[0], pos[1]):
                        self.pause = not self.pause
                        self.playPauseButton.changeImage()

                    # check if any of the menu buttons are clicked
                    for button in self.menu.buttons:
                        if button.buttonClicked(pos[0], pos[1]):
                            #conditons to check if the button is clicked and player has enough money
                            if button.get_buttonType() == 'short' and self.score >= 500:
                                self.score -= 500
                                self.isNewTower = True
                                #sets the type to know which tower to create
                                self.newTowerType = 'short'
                                # the function creates a new tower object based on type
                                self.addTower(self.newTowerType)
                            elif button.get_buttonType() == 'long' and self.score >= 750:
                                self.score -= 750
                                self.isNewTower = True
                                # sets the type to know which tower to create
                                self.newTowerType = 'long'
                                # the function creates a new tower object based on type
                                self.addTower(self.newTowerType)
                            elif button.get_buttonType() == 'range' and self.score >= 1000:
                                self.score -= 1000
                                self.isNewTower = True
                                # sets the type to know which tower to create
                                self.newTowerType = 'range'
                                # the function creates a new tower object based on type
                                self.addTower(self.newTowerType)
                            elif button.get_buttonType() == 'damage' and self.score >= 1000:
                                self.score -= 1000
                                self.isNewTower = True
                                # sets the type to know which tower to create
                                self.newTowerType = 'damage'
                                # the function creates a new tower object based on type
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



            # need to check if the game is paused or not, if not paused then perform the following actions
            if not self.pause:
                #loops through list of enemies
                for enemy in self.enemies:
                    # moves the enemy along the path
                    enemy.move()
                    #check their position to see if they made it all the way through the path
                    if enemy.pos_y > 700:
                        self.enemies.remove(enemy)

                        # remove a life if the enemy makes it through the whole path based on the damage property in enemy class
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
