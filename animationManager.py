"""A manager class to help avoid lag when updating sprites"""
import turtle
import collisionManager

class AnimationManager:
    def __init__(self, spriteList):
        self.spriteList = spriteList

        # A collision manager to encapsulate collision checking
        self.myCollisionManager = collisionManager.CollisionManager(spriteList = self.spriteList)

        turtle.tracer(False)

    def updateScreen(self):
        for sprite in self.spriteList:
            # Update each sprite in here rather than individually, so as to avoid lag
            sprite.updateSelf()
            
            # Check the sprites' coordinates
            if sprite.y >= 200 or sprite.y <= -200 or sprite.x >= 200 or sprite.x <= -200:
                sprite.undraw()
                # if outside of the window, remove sprite from spriteList
                self.spriteList.remove( sprite )
            
            # Check sprite collisons
            self.myCollisionManager.checkCollisions()
            
        turtle.update()

        # two "/" here for float division. 60 frames per second right now. 
        turtle.ontimer(self.updateScreen, 1000//60)  
        