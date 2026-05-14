"""A gui class to make tower placement more tower defense like"""
import turtle


class Graphical1:
    def __init__(self):
        # 1. define a box on the top right of the screen
        print("initiated")
        self.bottomX1, self.bottomY1 = 100, 100
        self.bottomX2, self.bottomY2 = 180, 100
        self.topX1, self.topY1 = 100, 180
        self.topX2, self.topY2 = 180, 180
        self.turt = turtle.Turtle()
        self.turt.hideturtle()
        self.turt.penup()
        self.clickCount = 0
    
    def draw(self):
        # 2. Visually define the box
        self.turt.goto(self.bottomX1,self.bottomY1)
        self.turt.pendown()
        self.turt.goto(self.bottomX2,self.bottomY2)
        self.turt.goto(self.topX2,self.topY2)
        self.turt.goto(self.topX1,self.topY1)
        self.turt.goto(self.bottomX1,self.bottomY1)

    def checkForClicks(self,x,y):
        # 3. Check for clicks within that box
        self.clickCount += 1 #Something besides a clickCount
        if self.bottomX1 < x < self.bottomX2 and self.bottomY1 < y < self.topY1:
            placeTowerOnNextClick = True
        return self.clickCount
# 	1. if clicked, add an attribute to the next click
# 4. Create a tower at the next player's click
# 	1. Check if the gui is clicked again
# Optional:
# 5. Have "deadzones" in which towers can't be placed(e.g. orc paths, on top of another tower).