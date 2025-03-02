"""A bullet class, subclass of the Sprite class"""
import turtle
import sprite

class Bullet(sprite.Sprite): #Inhertiance 

    def __init__(self, x, y, velx, vely):
        sprite.Sprite.__init__(self, x, y)
        # Add velocities to the constructor to enable shooting later on 
        self.velx = velx
        self.vely = vely
    
    def updateSelf(self):
        # The shooting of the bullet 
        self.x += self.velx
        self.y += self.vely
        
        self.turt.clear()
        self.turt.penup()
        self.turt.goto(self.x, self.y)
        self.turt.dot(5)

        # For now, Loop this until some end condition is met(e.g. a collision or leaving the screen)
        # This will likely need to be moved to the animation manager 
        turtle.ontimer(self.updateSelf, 500)