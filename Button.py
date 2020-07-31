import os
import pygame

class Button():
    def __init__(self, x, y, img):
        self.pos_x = x
        self.pos_y = y
        self.image = img
        self.type = None


    #draws button onto screen given x and y parameters passed into the constructor
    def drawButton(self,window):
        window.blit(self.image, (self.pos_x, self.pos_y))

    def buttonClicked(self, X, Y):
        """
        returns true of false depending on whether the button is clicked given x and y coordinates
        """

        # checks to see if the click is within the range of the image
        if X >= self.pos_x  and X<= self.pos_x + self.image.get_width():
            if Y>= self.pos_y  and  Y<= self.pos_y + self.image.get_height() :
                return True


        return False

    def get_buttonType(self):
        return self.type

class PlayPauseButton(Button):
    def __init__(self, x, y, playImg, pauseImg):
        self.pos_x = x
        self.pos_y = y
        self.image = playImg
        self.playImage = playImg
        self.pauseImage = pauseImg

    def changeImage(self):
        if self.image == self.playImage:
            self.image = self.pauseImage
        else:
            self.image = self. playImage