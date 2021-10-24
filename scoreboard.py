from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 235)
        self.hideturtle()
        self.color("White")
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def display_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
