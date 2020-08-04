import os
import pygame
from Menu import UpgradeMenu
import math

'''
Abstract class 
'''
class Tower:
    def __init__(self, x, y):
        self.tower_images=[]
        #keeps track of the price of the tower each level
        self.price = [0,0,0]
        #keeps track of the selling price of the tower at each level
        self.sell_price = [0,0,0]
        self.level= 1
        self.damage= 1
        self.initialDamage= self.damage

        self.range = 0
        self.initialRange = self.range

        #position of the tower
        self.pos_x = x
        self.pos_y = y

        self.width = 64
        self.height = 64

        #pass in x and y coordinates and adjust them accordingly to display under he tower
        self.upgradeMenu = UpgradeMenu( self.pos_x - self.width , self.pos_y , self)

        self.isSelected = False
        self.showMenu = False

        self.place_color = (0,0,255, 100)

    #draws the range radius of the tower if it is clicked
    def drawRadius(self, window):
        # draw range of transparent circle only if isSelected is true
        if self.isSelected:
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (169, 169, 169, 100), (self.range, self.range), self.range, 0)
            window.blit(surface, (self.pos_x - self.range, self.pos_y - self.range))

    # draws teh radius of the tower, used for placement
    def drawPlacement(self, window):
        surface = pygame.Surface((32 * 4, 32* 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (40, 40), 40, 0)
        window.blit(surface, (self.pos_x - 40 , self.pos_y -40))

    #draws the tower onto the window
    def drawTower(self, window):
        #because level starts at one have to decrement by 1
        img = self.tower_images[self.level - 1]
        window.blit(img, (self.pos_x - img.get_width()//2, self.pos_y - img.get_height()//2))
        self.drawRadius(window)

        #if show menu is true then draw it onto the screen
        if self.showMenu:
            self.upgradeMenu.drawMenu(window)


    def click(self, X, Y, score):
        """
        checks to see if the tower is clicked
        true if the click matches the towers position, else return false
        :param X: x coordinate of click
        :param Y: y coordinate of click
        :return: returns the cost of the upgrade, if the upgrade button is clicked returns the cost so it can be deducted from the players money
                other wise returns 0 because nothing is purchased
        """
        upgrade_cost = 0
        #changes state of the isSelected accordingly if the click is with range of the tower
        if X >= self.pos_x - self.width//2  and X<= self.pos_x + self.width//2:
            if Y>= self.pos_y - self.height//2 and  Y<= self.pos_y + self.height//2 :
                self.isSelected= True
                #menu only shows if the tower is clicked
                self.showMenu= True


            else:
                self.isSelected = False
                self.showMenu = False
        else:
            self.isSelected = False
            self.showMenu = False

        '''
        both the else checks are needs so that if either position of the X or Y click is not in range, the radius will not show
        if only one of them is there, radius will show if either of the conditions is true
        '''

        # if one of the upgrade button is clicked then isSelected and showMenu is True and we still need to show the menu
        if self.upgradeMenu.button.buttonClicked(X, Y):
            self.isSelected = True
            self.showMenu = True

            #if the upgrade button is clicked then we have to perform the upgrade
            if score >= self.get_upgradeCost():
                upgrade_cost = self.get_upgradeCost()
                #perform upgrade
                self.upgrade()
        return upgrade_cost




    #sells the tower and returns an int, which is the sell price
    def sell(self):
        return self.sell_price[self.level - 1]

    #increments the tower level and damage upon upgrade
    def upgrade(self):
        if(self.level < len(self.tower_images)):
            self.level += 1
            self.damage +=1
            self.initialDamage +=1

    #returns the cost of the next tower price
    def get_upgradeCost(self):
        if(self.level < len(self.tower_images)):
            return self.price[self.level]

    #checks if a tower is on top of another tower when being placed on the map
    def collide(self, tower):
        x2 = tower.pos_x
        y2 = tower.pos_y

        distance = math.sqrt( math.pow(x2 - self.pos_x, 2) + math.pow(y2 - self.pos_y, 2))
        if distance >= 80:
            return False
        else:
            return True
