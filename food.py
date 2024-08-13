import random
from turtle import *
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("yellow")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        xpos = random.randrange(-280,280)
        ypos = random.randrange(-280,280)
        self.goto(xpos, ypos)
