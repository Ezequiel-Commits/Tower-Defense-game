"""A Sprite superclass for different objects in my game(Tower, bullet, orc, etc.)"""
import turtle

class Sprite:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

        self.turt = turtle.Turtle()
        self.turt.ht()

    def command(self):
        pass

    def drawCircle(self):
        self.turt.penup()
        self.turt.goto(self.x, self.y)
        self.turt.forward(self.size/2)
        self.turt.right(90)
        self.turt.forward(self.size*1.5)
        self.turt.pendown()
        
        self.turt.left(90)
        self.turt.circle(self.size)
        # self.turt.right(90)
        # self.turt.backward(self.x)

    def draw(self):
        self.turt.penup()
        self.turt.goto(self.x,self.y)
        self.turt.pendown()
        # Draw a circle given a center x and y

    def undraw(self):
        # This doesn't get rid of the turtles. I'd hope that doesn't cause enough lag to be noticable.
        self.turt.clear()
        print("Undraw called")
