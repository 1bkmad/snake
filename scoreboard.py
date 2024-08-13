from turtle import Turtle, Screen
FONT = ('Comic Sans MS', 18, 'normal')
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"score = {self.score} ", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def score_increment(self):
        self.score += 1
        self.clear()

        self.write(f"score = {self.score} ", move=False, align=ALIGNMENT, font=FONT)
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER !! ", move=False, align=ALIGNMENT, font=FONT)
