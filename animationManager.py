"""A manager class to help avoid lag when updating sprites"""
import sys
import turtle
import collisionManager
import tower
import bullet
import orcFactory
import random

class AnimationManager:
    def __init__(self, spriteList):
        self.spriteList = spriteList

        # A collision manager to encapsulate collision checking
        self.myCollisionManager = collisionManager.CollisionManager(spriteList = self.spriteList)

        self.frameCount = 0

        turtle.tracer(False)

    def updateScreen(self):

        if self.frameCount % 20 == 0:
                # Create a new orc if 60 frames have passed. 

                # Add a random y value eventually
                myFactory = orcFactory.OrcFactory(x = -199, y = 0, size = 15)
                # Somewhere in constructing this orc, I'll want to add a path for it to follow. 
                newOrc = myFactory.createOrc()
                # print("=== 60 frames passed ===")
                self.spriteList.append( newOrc ) 

        for sprite in self.spriteList:
            # Update each sprite in here rather than individually, so as to avoid lag
            sprite.updateSelf()
            
            if sprite.y >= 200 or sprite.y <= -200 or sprite.x >= 200 or sprite.x <= -200:
                # Check the sprites' coordinates
                
                # if outside of the window, undraw the sprite and remove the sprite from spriteList 
                sprite.undraw()
                self.spriteList.remove( sprite )
            
            if isinstance(sprite, tower.Tower):
                # Check if the sprite is a tower
                if self.frameCount % 60 == 0:
                    # Check if it's been 60 frames since the last time a bullet was fired.  
                    
                    # Additionally, two bullets fire the first time this runs 
                    myNewBullet = bullet.Bullet(x = sprite.x, y = sprite.y, velX = 0, \
                                                velY = -1, size = 5)
                    
                    self.spriteList.append( myNewBullet ) 

            if self.myCollisionManager.checkCollisions() == 1: # Check collisons between sprite pairs
                sys.exit("game over")
            else:
                pass
        self.frameCount += 1 # Add 1 to the frame count each time this function is called
            
        turtle.update()

        # two "/" here for float division. 60 frames per second right now. 
        turtle.ontimer(self.updateScreen, 1000//60)  
        