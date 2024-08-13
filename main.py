import turtle
from turtle import Turtle, Screen
import time
from snake import *
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")


screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


snake.snake_body_function()
screen.update()
game_is_on = True
score = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_movement()

    #Detecting collison
    if (snake.snake_body[0].distance(food) <= 15):
        food.refresh()
        snake.extend()
        scoreboard.score_increment()


    #Detect colision with wall.
    if snake.snake_body[0].xcor()  > 280 or snake.snake_body[0].xcor()  < -280 or snake.snake_body[0].ycor() > 280 or snake.snake_body[0].ycor() < -280 :
        game_is_on = False
        scoreboard.game_over()

    #Detect colision with body.
    #if head touches any part of body, game over
    for segment in snake.snake_body[1:]:    #slicing from position 1 to end of list
        if snake.snake_body[0].distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
