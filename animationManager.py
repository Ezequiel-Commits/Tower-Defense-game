"""A manager class to help avoid lag when updating sprites"""
import turtle

class AnimationManager:
    def __init__(self, spriteList):
        self.spriteList = spriteList
        turtle.tracer(False)

    def updateScreen(self):
        for sprite in self.spriteList:
            # Update each sprite in here rather than individually, so as to avoid lag
            sprite.updateSelf()
        turtle.update()
        turtle.ontimer(self.updateScreen, 1000//60) # two "/" here for float division. 
        