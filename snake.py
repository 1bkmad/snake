import turtle
from turtle import Turtle
import time

MOVE_DISTANCE = 20

"""
snake_body_function defines the body of snake like it will have 3 blocks as initial
body length, shape will be square, the starting position, etc. 
"""

"""
setheading works with absolute directional angle where as left() or right() work
with relative angle.
"""

class Snake:
    def __init__(self):
        self.snake_body = []
        self.pos = 0
        self.game_is_on = True


    def snake_body_function(self):
        for _ in range(3):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(self.pos, 0)
            self.pos -= 20
            self.snake_body.append(tim)


    def extend(self):
        tim = Turtle("square")
        tim.penup()
        tim.color("white")
        tim.goto(self.snake_body[-1].position())
        self.snake_body.append(tim)

    def snake_movement(self):
        time.sleep(0.1)
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)
    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)
