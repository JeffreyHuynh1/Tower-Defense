import os
import pygame
from Enemy import Enemy

#loops through the images in the enemy1 folder and adds the 64x64 images into the images list
imgs = []
for i in range(0,20):
    str_add = str(i)
    if(i>=10):
        e = pygame.image.load(os.path.join("enemies/enemy3", "0_boss_run_0" + str_add + ".png"))
    else:
        e = pygame.image.load(os.path.join("enemies/enemy3", "0_boss_run_00" + str_add + ".png"))
    e = pygame.transform.scale(e, (128,128))
    imgs.append(e)

class Boss(Enemy):
    def __init__(self):
        super().__init__()
        self.images = imgs[:]
        self.height = 128
        self. width = 128
        self.health = 5
        self.initial_health= 5