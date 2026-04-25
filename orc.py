"""An Orc class, subclass of the Sprite class"""
import sprite
import turtle

checkpointsForMap1 = [[-50,0],[-50,100],[75,100],[75,0],[150,0]]
# reachedpoint0 = False

class Orc(sprite.Sprite):
    # Use the sprite constructor
    def __init__(self, x, y, size):
        # add a specific init function for orc pathing
        super().__init__(x, y, size)
        self.reachedpoint0 = False
        self.reachedpoint1 = False
        self.reachedpoint2 = False
        self.reachedpoint3 = False
        self.reachedpoint4 = False
    
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
        # Path variables; feel a bit redundant
        point0 = checkpointsForMap1[0]
        #Replacing this variable with the coordinates of the first point? 

        # Iteration through checkpoints
        if self.x < checkpointsForMap1[0][0] and self.reachedpoint0 == False:
            # If the orc hasn't reached the first point, move toward that point 
            self.x += 3
            self.turt.clear()
            self.draw()
        elif self.y < checkpointsForMap1[1][1] and self.reachedpoint1 == False:
            # If the orc has reached the first point, move toward the second point
            self.y += 3
            self.turt.clear()
            self.draw()
            self.reachedpoint0 = True
        elif self.x < checkpointsForMap1[2][0] and self.reachedpoint2 == False:
            self.x += 3
            self.turt.clear()
            self.draw()
            self.reachedpoint1 = True
        elif self.y > checkpointsForMap1[3][1] and self.reachedpoint3 == False:
            self.y -= 3
            self.turt.clear()
            self.draw()
            self.reachedpoint2 = True
        elif self.x < checkpointsForMap1[4][0] and self.reachedpoint4 == False:
            self.x += 3
            self.turt.clear()
            self.draw()
            self.reachedpoint3 = True