"""A bullet class, subclass of the Sprite class"""
import turtle
import sprite

class Bullet(sprite.Sprite): #Inhertiance 

    def __init__(self, x, y, velX, velY):
        sprite.Sprite.__init__(self, x, y)
        # Add velocities to the constructor to enable shooting later on 
        self.velX = velX
        self.velY = velY
    
    def updateSelf(self):
        # The shooting of the bullet 
        self.x += self.velX
        self.y += self.velY
        print(self.y)
        
        self.turt.clear()
        self.turt.penup()
        self.turt.goto(self.x, self.y)
        self.turt.dot(5)