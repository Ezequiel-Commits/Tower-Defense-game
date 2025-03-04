"""A tower class, subclass of the Sprite class"""
import sprite
import bullet
import time

class Tower(sprite.Sprite): #Inhertiance 

    def __init__(self, x, y, size, bullet):
        sprite.Sprite.__init__(self, x, y, size)
        # pass in a bullet object here so as to avoid creating bullet objects later
        self.myBullet = bullet


    def draw(self):
        sprite.Sprite.draw(self)
        # Overwrite the superclass' draw method
        for i in range(4):
            self.turt.forward(self.size)
            self.turt.right(90)
        self.drawCircle()

    def updateSelf(self):
        self.draw()    
        # Creating an if statement to check whether or not a new bullet should be made
            