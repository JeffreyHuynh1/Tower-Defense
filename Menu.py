import os
import pygame
from Button import Button

pygame.font.init()

'''
class for Menu 
'''
class Menu():
    def __init__(self,x,y):
        self.pos_x = x
        self.pos_y = y
        self.image = pygame.image.load(os.path.join('assets', 'menu.png'))

    #draws menu onto the window based on the x and y coordinates passed into the constructor
    def drawMenu(self, window):
        window.blit(self.image, (self.pos_x, self.pos_y))


'''
each tower has an upgrade menu attached to it that allows for upgrade of the tower
'''
class UpgradeMenu(Menu):
    def __init__(self, x, y,tower):
        super() .__init__(x,y)
        self.image = pygame.transform.scale(self.image, (120, 60))
        #cost of the upgrades for tower
        self.upgradePrice = [200, 500, 'Max']

        self.upgradeImage = pygame.transform.scale( pygame.image.load(os.path.join('assets', 'arrow.png')) , (50,50))
        self.jewelImage = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'jewel.png')), (35, 35))
        self.button = Button(self.pos_x + 10 , self.pos_y + 5, self.upgradeImage)

        self.font = pygame.font.Font('freesansbold.ttf', 25)

        #passing in the tower that this upgradeMenu is associated with
        self.tower = tower

    #draws the menu underneath the tower
    def drawMenu(self,window):
        super().drawMenu(window)

        self.button.drawButton(window)
        self.button.type = "Upgrade"

        #displays jewel icon into the menu bar
        window.blit(self.jewelImage, (self.pos_x + self.image.get_width() - self.jewelImage.get_width() - 10 , self.pos_y + 5))

        #displays the cost of the upgrade onto the menu
        text = self.font.render(str(self.tower.get_upgradeCost()), True, (255,255,255))
        window.blit(text, (self.pos_x + self.image.get_width() - self.jewelImage.get_width() - 10,self.pos_y + 38 ))

class MainMenu(Menu):
    def __init__(self, x, y):
        super() .__init__(x,y)
        self.image = pygame.transform.scale(self.image, (70, 300))
        self.rangeImg = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'range.png')), (50, 50))
        self.damageImg = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'damage.png')), (50, 50))
        self.shortImg = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'short.png')), (50, 50))
        self.longImg = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'long.png')), (50, 50))

        self.jewelImage = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'jewel.png')), (15, 15))

        self.buttonShort = Button( 10, self.pos_y + 10, self.shortImg)
        self.buttonLong = Button( 10, self.pos_y + (self.image.get_height() * .25) + 5, self.longImg)
        self.buttonRange = Button(10, self.pos_y + (self.image.get_height() * .5), self.rangeImg)
        self.buttonDamage = Button(10, self.pos_y + (self.image.get_height() * .75), self.damageImg)

        self.buttons = [self.buttonShort, self.buttonLong, self.buttonRange, self.buttonDamage]

        self.font = pygame.font.Font('freesansbold.ttf', 15)

    def drawMenu(self, window):
        super().drawMenu(window)

        self.buttonRange.drawButton(window)
        self.buttonRange.type = 'range'

        self.buttonDamage.drawButton(window)
        self.buttonDamage.type = 'damage'

        self.buttonShort.drawButton(window)
        self.buttonShort.type = 'short'

        self.buttonLong.drawButton(window)
        self.buttonLong.type = 'long'

        window.blit(self.jewelImage, (0, self.pos_y + 60 ))
        window.blit(self.jewelImage,( 0, self.pos_y + (self.image.get_height() * .25) + 55))
        window.blit(self.jewelImage,(0, self.pos_y + (self.image.get_height() * .5) + 50))
        window.blit(self.jewelImage,(0, self.pos_y + (self.image.get_height() * .75) + 50))

        # displays the cost of towers onto the menu
        textShort = self.font.render('500', True, (255, 255, 255))
        window.blit(textShort, (self.buttonRange.pos_x/2 + 15, self.pos_y + 60 ))

        textLong = self.font.render('750', True, (255, 255, 255))
        window.blit(textLong, (self.buttonRange.pos_x / 2 + 15, self.pos_y + (self.image.get_height() * .25) + 55))

        textSupport = self.font.render('1000', True, (255, 255, 255))
        window.blit(textSupport, (self.buttonRange.pos_x / 2 + 15, self.pos_y + (self.image.get_height() * .5) + 50))

        window.blit(textSupport, (self.buttonRange.pos_x / 2 + 15, self.pos_y + (self.image.get_height() * .75) + 50))





