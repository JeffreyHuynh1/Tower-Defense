import os
import pygame


class Button():
    def __init__(self, x, y, img):
        self.pos_x = x
        self.pos_y = y
        self.image = img


    #draws button onto screen given x and y parameters passed into the constructor
    def drawButton(self,window):
        window.blit(self.image, (self.pos_x, self.pos_y))

    def buttonClicked(self, X, Y):
        """
        returns true of false depending on whether the button is clicked given x and y coordinates
        """
        #print('X ' + str(X))
        #print('self.x ' + str(self.pos_x))
        #print('X left ' + str(self.pos_x - self.image.get_width()//2))
        #print('X right ' + str(self.pos_x + self.image.get_width()//2))
        if X >= self.pos_x  and X<= self.pos_x + self.image.get_width():
            #print('in x')
            if Y>= self.pos_y  and  Y<= self.pos_y + self.image.get_height() :
                #print('is clicked')
                return True

        #print('nope')
        return False