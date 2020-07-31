from Tower import Tower
import os
import pygame
import math
import time

'''
import images for range and attack towers
'''
rangeImg= []
damageImg= []
#loads the tower images into the list
for i in range(5, 7):
    str_add = str(i)
    tower = pygame.image.load(os.path.join("towers/supportTower",  str_add + ".png"))
    tower = pygame.transform.scale(tower, (64, 64))
    rangeImg.append(tower)

for i in range(8, 10):
    str_add = str(i)
    tower = pygame.image.load(os.path.join("towers/supportTower",  str_add + ".png"))
    tower = pygame.transform.scale(tower, (64, 64))
    damageImg.append(tower)




'''
gives more range to towers in the radius
'''
class RangeTower(Tower):
    def __init__(self, x, y):
        super(). __init__( x, y)
        self.range = 150
        self.effect = [.2, .4]
        self.tower_images = rangeImg[:]


    def support(self, towers):
        """
        adds range to towers in its radius according to level
        :param towers: takes in list of towers
        :return:  None
        """
        effected = []
        for tower in towers:
            x = tower.pos_x
            y = tower.pos_y

            distance = math.sqrt(math.pow(self.pos_x - x, 2) + math.pow(self.pos_y - y, 2))

            #checks to see if the tower is in range
            if distance  <= self.range + tower.width/2:
                effected.append(tower)

            for tower in effected:
                tower.range = tower.initialRange + round(tower.initialRange * self.effect[self.level - 1])


class DamageTower(RangeTower):
    def __init__(self, x, y):
        super(). __init__( x, y)
        self.range = 100
        self.effect = [.2, .4]
        self.tower_images = damageImg[:]

    def support(self, towers):
        effected = []
        for tower in towers:
            x = tower.pos_x
            y = tower.pos_y

            distance = math.sqrt(math.pow(self.pos_x - x, 2) + math.pow(self.pos_y - y, 2))

            # checks to see if the tower is in range
            if distance  <= self.range + tower.width/2:
                effected.append(tower)

            for tower in effected:
                tower.damage = tower.initialDamage + (tower.initialDamage * self.effect[self.level - 1])

