import os
import pygame
import math

#super class for enemy
class Enemy:
    def __init__(self):
        self.images=[]
        self.img= None
        self.animation_count = 0
        self.path = [(22, 530), (149, 511), (199, 389), (233, 320), (341, 289), (389, 136), (453, 91), (952, 91), (1002, 144),
                     (1005, 256), (940, 304), (840, 346), (822, 423), (864, 506), (929, 530), (1002, 569), (1019, 682)]
        self.pos = 0
        self.pos_x= self.path[self.pos][0]
        self.pos_y = self.path[self.pos][1]
        self.health = 100

    def move(self):
        """
        traverses through the path array which contains a list of points , need to calculate the distance between points
        :return:
        """

        #get starting position of enemy x,y, and get the next point where they need to travel to
        x1, y1 = self.path[self.pos]

        #check if the next point is within bounds
        if self.pos + 1 < len(self.path):
            x2, y2 = self.path[self.pos + 1]
            #print(x2, y2)

        #we are at the last point in the path, set x2,y2
        else:
            x2, y2 = (1019, 710)

        change_x, change_y = (x2 - x1, y2- y1)

        # this is the distance between two of the points
        distance = math.sqrt(math.pow(change_x, 2) + math.pow(change_y, 2))
        print('This is the distance: ' + str(distance))

        vel = .1

        self.pos_x += change_x * vel
        self.pos_y += change_y * vel

        print('This is position x: ' + str(self.pos_x))
        print('This is position y: ' + str(self.pos_y))

        #this is the distance that we have currently traveled
        disance_traveled = math.sqrt(math.pow((self.pos_x - x1), 2) + math.pow((self.pos_y - y1), 2))
        print('This is the distance traveled:' + str(disance_traveled))

        #if the distance traveled is greater than the distance between the two points
        # we have to update the position in the path list accordingly
        if disance_traveled >= distance:
            #make sure that we are travelling within the points in the list
            #check to see if we will go out of bounds
            if self.pos+1 < len(self.path):
                self.pos += 1
                print('new position in path' + str(self.pos))







    def drawEnemy(self, window):
        """
        draws the enemy onto the window
        :param window:
        :return:
        """

        #grab specific image, program will be running at 30fps so each image will get 3 seconds for display
        self.img= self.images[self.animation_count//3]
        self.animation_count += 1

        #once the end of the list is hit, set the animation count back to 0
        if self.animation_count >= len(self.images)*3:
            self.animation_count=0

        #display the image on to the window, want to blit on self.pos_y - 32 so that the image is centered at the point considering that image is 64x64
        window.blit(self.img, (self.pos_x, self.pos_y-32))
        #moves the enemy along the path
        self.move()
