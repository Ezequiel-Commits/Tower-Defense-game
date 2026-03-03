"""An Orc class, subclass of the Sprite class"""
import sprite
import turtle

class Orc(sprite.Sprite):
    # Use the sprite constructor
    
    def draw(self):
        # Draw a triangle to represent orcs for now
        sprite.Sprite.draw(self) #Go to the x and y passed in the constructor
        for i in range(3):
            self.turt.forward(self.size)
            self.turt.right(120)
        self.drawCircle()

    def updateSelf(self):
        # Follow a path
        
        self.draw()
        # Path variables
        point1 = [210,0]
        reachedPoint1 = False

        if self.x < point1[0] and reachedPoint1 == False:
            # If the orc hasn't reached the first point, move toward that point 
            self.x += 3
            self.turt.clear()
            self.draw()
        else:
            reachedPoint1 == True