"""A manager to check for collisions between objects each time the screen is updated."""
import math
import turtle

class CollisionManager:
    def __init__(self, spriteList):
        self.spriteList = spriteList
        self.reference = self.spriteList[0]
    
    def checkCollisions(self):
        # Use bounding circles to check if one sprite has collided with another
        for sprite in self.spriteList:
            if sprite != self.reference: #Avoid looking at the same sprite 
                print(sprite)
                # Check for collisions using the math.dist method
                distanceBetweenSprites = math.dist([sprite.x, sprite.y],[self.reference.x, self.reference.y])
                if distanceBetweenSprites <= self.reference.size + sprite.size:
                    # If the distance between two sprites is less than the combined radii of their
                    # bounding circles, an overlap is present
                    print("overlap deteced")
                    # Remove the sprite's drawing and the remove the sprite from the spriteList
                    sprite.undraw()

                    self.spriteList.remove( sprite )

                self.reference = sprite #Change the reference sprite after we've checked against 
                # a new sprite
        
            