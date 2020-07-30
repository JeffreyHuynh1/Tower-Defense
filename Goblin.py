import os
import pygame
from Enemy import Enemy

#loops through the images in the enemy1 folder and adds the 64x64 images into the images list
imgs=[]
for i in range(0,10):
    str_add = str(i)
    e = pygame.image.load(os.path.join("enemies/enemy1", "2_enemies_1_RUN_00" + str_add + ".png"))
    e = pygame.transform.scale(e, (64,64))
    imgs.append(e)

class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.images= imgs[:]
        self.width= 64
        self.height = 64
        self.health = 2
        self.initial_health= 2

        self.damage = 1
        self.money = self.initial_health * 100

