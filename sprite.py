"""A Sprite superclass for different objects in my game(Tower, bullet, orc, etc.)"""
import turtle

class Sprite:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.turt = turtle.Turtle()
        self.turt.ht()

    def command(self):
        pass

    def draw(self):
        self.turt.penup()
        self.turt.goto(self.x,self.y)
        self.turt.pendown()

    def undraw(self):
        pass