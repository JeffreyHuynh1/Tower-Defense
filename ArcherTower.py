from Tower import Tower
import os
import pygame
import math
import time

class ArcherTower(Tower):
    def __init__(self, x, y):
        super() .__init__(x, y)
        self.archer_images = []
        self.archer_count = 0
        self.range = 100
        self.initialRange = 100
        self.inRange = False
        self.isLeft = False
        self.damage = 1.25
        self.initialDamage=1.25
        self.hit_timer = pygame.time.get_ticks()
        self.cooldown = 700
        self.price = [750,1000,1250]

        #loads the tower images into the list
        for i in range(7, 10):
            str_add = str(i)
            tower = pygame.image.load(os.path.join("towers/archerTower",  str_add + ".png"))
            tower = pygame.transform.scale(tower, (64, 64))
            self.tower_images.append(tower)


        #loads the archer images into the archer image list
        for i in range(38, 44):
            str_add = str(i)
            archer = pygame.image.load(os.path.join("towers/archerTower/archers",  str_add + ".png"))
            archer = pygame.transform.scale(archer, (32, 32))
            self.archer_images.append(archer)


    def drawTower(self, window):

        super().drawTower(window)

        #only if the there is an enemy in range is when the animation for attacking appears
        if self.inRange:
            self.archer_count += 1

            # checks to see if archer count is within range of the archer_images list
            if self.archer_count >= len(self.archer_images) * 3:
                self.archer_count = 0

        else:
            self.archer_count = 0


        archer = self.archer_images[self.archer_count // 3]
        # gets the archer on the centered at the top of the tower
        window.blit(archer, (self.pos_x - (self.width / 2) + (archer.get_width() / 2), (self.pos_y - self.height) + archer.get_height() / 2))


    #changes the range of the tower according to the parameter
    def changeRange(self, r):
        self.range = r


    def attack(self, enemies):
        """
        given a list of enemies, determines if the tower should attack enemies based on the range
        :return: deals damage to the enemies and returns value based on whether or not an enemy is destroyed
        """
        money = 0
        self.inRange = False
        enemy_closest = []

        for enemy in enemies:
            enemy_x = enemy.pos_x
            enemy_y = enemy.pos_y


            #calculate the distance between the tower and the position of the enemy
            dist = math.sqrt( math.pow(enemy_x - self.pos_x, 2) + math.pow(enemy_y - self.pos_y, 2))

            if dist <= self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        #sorts the enemy based on the x position of the enemy
        enemy_closest.sort(key=lambda enemy: enemy.pos_x)

        #make sure that there are elements in range in the enemy closest list
        if len(enemy_closest) > 0:
            #grab the closest enemy which is the first element because the list is sorted
            first_enemy = enemy_closest[0]


            # This is for the cooldown, every 700 miliseconds the tower will fire
            now = pygame.time.get_ticks()
            if now - self.hit_timer >= self.cooldown:
                self.hit_timer = now

                # calculate the damage inflicted on the enemy
                first_enemy.health -= self.damage
                #if the health bar drops to 0, remove the enemy from the list
                if(first_enemy.health<= 0):
                    # set money to the enemies money property because they killed it and should be added to score
                    money = first_enemy.money
                    enemies.remove(first_enemy)

            #if the enemy is on the left of the tower and the isLeft property is false
            if first_enemy.pos_x < self.pos_x and not self.isLeft:
                self.isLeft = True

                # perform a horizontal flip on the archer images
                for i, img in enumerate(self.archer_images):
                    self.archer_images[i] = pygame.transform.flip(img, True, False)

            #if the enemy is on the right of the tower and the isLeft property is set to true
            elif first_enemy.pos_x > self.pos_x and self.isLeft:
                self.isLeft = False
                for i, img in enumerate(self.archer_images):
                    self.archer_images[i] = pygame.transform.flip(img, True, False)

        return money



# loads the tower images into the list
towerShortImages = []
towerShortArcher = []
for i in range(2, 5):
    str_add = str(i)
    tower = pygame.image.load(os.path.join("towers/archerTower", str_add + ".png"))
    tower = pygame.transform.scale(tower, (64, 64))
    towerShortImages.append(tower)

# loads the archer images into the archer image list
for i in range(64, 70):
    str_add = str(i)
    archer = pygame.image.load(os.path.join("towers/archerTower/archers", str_add + ".png"))
    archer = pygame.transform.scale(archer, (32, 32))
    towerShortArcher.append(archer)


class ArcherTowerShort(ArcherTower):
    def __init__(self, x, y):
        super() .__init__(x, y)
        self.archer_images = []
        self.range = 125
        self.initialRange=150
        self.damage = 1
        self.initialDamage =1
        self.cooldown = 700
        self.price = [500, 750, 1000]
        self.archer_images = towerShortArcher[:]
        self.tower_images = towerShortImages[:]


