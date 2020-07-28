import os
import pygame

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

        #position of the tower
        self.pos_x = x
        self.pos_y = y

        self.width = 0
        self.height = 0

        self.isSelected = False

    #draws the tower onto the window
    def drawTower(self, window):
        #because level starts at one have to decrement by 1
        img = self.tower_images[self.level - 1]
        window.blit(img, (self.pos_x - img.get_width()//2, self.pos_y - img.get_height()//2))


    def click(self):
        pass

    #sells the tower and returns an int, which is the sell price
    def sell(self):
        return self.sell_price[self.level - 1]

    #increments the tower level and damage upon upgrade
    def upgrade(self):
        if(self.level < len(self.tower_images)):
            self.level += 1
            self.damage +=1

    #returns the cost of the next tower price
    def get_upgradeCost(self):
        if(self.level < len(self.tower_images)):
            return self.price[self.level]

    def move(self):
        pass
