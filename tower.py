"""A tower class, subclass of the Sprite class"""
import sprite
import bullet
import time

class Tower(sprite.Sprite): #Inhertiance 

    # No need for a constructor unless I want new attributes in this class. 

    def draw(self):
        sprite.Sprite.draw(self)
        # Overwrite the superclass' draw method
        for i in range(4):
            self.turt.forward(10)
            self.turt.right(90)

    def updateSelf(self):
        # Create and Shoot out bullets(objects of the bullet class)
        self.draw()    
        # Right now this is creating multiple bullets that update themselves once only
        myBullet = bullet.Bullet(x = self.x, y = self.y, velX = 2, velY = 2)
        myBullet.updateSelf()