"""An Orc class, subclass of the Sprite class"""
import sprite
import turtle

class Orc(sprite.Sprite):
    # Use the sprite constructor
    
    def draw(self):
        # Draw a triangle to represent orcs for now
        sprite.Sprite.draw(self) #Go to the x and y passed in the constructor
        for i in range(3):
            self.turt.forward(5)
            self.turt.right(120)

    def updateSelf(self):
        # Follow a path
        self.draw()
        # Path variables
        point1 = [-20,20]
        reached1 = False
        point2 = [-20,0]
        reached2 = False
        if self.x > -100 and reached1 == False:
            # If the orc hasn't reached the first point, move toward that point 
            self.x -= 1
            self.turt.clear()
            self.draw()
        else:
            reached1 == True