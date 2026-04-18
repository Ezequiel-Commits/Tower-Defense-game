"""An Orc class, subclass of the Sprite class"""
import sprite
import turtle

checkpointsForMap1 = [[-50,0]]
# reachedpoint0 = False

class Orc(sprite.Sprite):
    # Use the sprite constructor
    # add a specific init function
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.reachedpoint0 = False
    
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
        point0 = checkpointsForMap1[0]
        #Replacing this variable with the coordinates of the first point? 

        # Iteration through checkpoints
        if self.x < point0[0] and self.reachedpoint0 == False:
            # If the orc hasn't reached the first point, move toward that point 
            self.x += 3
            self.turt.clear()
            self.draw()
        elif self.x >= point0[0]:
            # If the orc has reached the first point, move toward the second point
            print("reached")
            self.y += 3
            self.turt.clear()
            self.draw()
            self.reachedpoint0 = True
        # elif self.y 
        else:
            pass