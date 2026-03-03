"""If the orcs enter the gatehouse, the game should end"""
import sprite

class Gatehouse(sprite.Sprite):
    
    def draw(self):
        sprite.Sprite.draw(self)
        for i in range(2):
            # Draw a gatehouse(rectangle) by the end of the orcs' path
            # x and y are equivalent to leftX and topY
            self.turt.right(90)
            self.turt.forward(self.size)
            self.turt.right(90)
            self.turt.forward(self.size/4)
        self.drawCircle() # Doesn't work the best for this sprite 
    
    def updateSelf(self):
        self.draw()

