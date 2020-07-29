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

        self.range = 0

        #position of the tower
        self.pos_x = x
        self.pos_y = y

        self.width = 0
        self.height = 0

        self.isSelected = False

    #draws the range radius of the tower if it is clicked
    def drawRadius(self, window):
        # draw range of transparent circle only if isSelected is true
        if self.isSelected:
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (169, 169, 169, 100), (self.range, self.range), self.range, 0)
            window.blit(surface, (self.pos_x - self.range, self.pos_y - self.range))


    #draws the tower onto the window
    def drawTower(self, window):
        #because level starts at one have to decrement by 1
        img = self.tower_images[self.level - 1]
        window.blit(img, (self.pos_x - img.get_width()//2, self.pos_y - img.get_height()//2))
        self.drawRadius(window)

    def click(self, X, Y):
        """
        checks to see if the tower is clicked
        :param X: x coordinate of click
        :param Y: y coordinate of click
        :return: true if the click matches the towers position, else return false
        """

        #changes state of the isSelected accordingly if the click is with range of the tower
        if X >= self.pos_x - self.width//2  and X<= self.pos_x + self.width//2:
            if Y>= self.pos_y - self.height//2 and  Y<= self.pos_y + self.height//2 :
                self.isSelected= True
            else:
                self.isSelected = False
        else:
            self.isSelected = False

        '''
        both the else checks are needs so that if either position of the X or Y click is not in range, the radius will not show
        if only one of them is there, radius will show if either of the conditions is true
        '''


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
