import os
import pygame
from Enemy import Enemy

class Beast(Enemy):
    def __init__(self):
        super().__init__()

        #loops through the images in the enemy1 folder and adds the 64x64 images into the images list
        for i in range(0,10):
            str_add = str(i)
            e = pygame.image.load(os.path.join("enemies/enemy2", "2_enemies_1_RUN_00" + str_add + ".png"))
            e = pygame.transform.scale(e, (64,64))
            self.images.append(e)