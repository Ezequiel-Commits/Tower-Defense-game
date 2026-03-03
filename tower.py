"""A tower class, subclass of the Sprite class"""
import sprite
import bullet
import time

class Tower(sprite.Sprite): #Inhertiance 

    def __init__(self, x, y, size):
        sprite.Sprite.__init__(self, x, y, size)


    def draw(self):
        sprite.Sprite.draw(self)
        # Overwrite the superclass' draw method
        for i in range(4):
            self.turt.forward(self.size)
            self.turt.right(90)
        self.drawCircle()

    def updateSelf(self):
        self.draw()    
            