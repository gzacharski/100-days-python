from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape(None)
        self.a_score = 0
        self.goto(0, 260)
        self.color("white")
        self.refresh()

    def refresh(self):
        self.write(f"Score: {self.a_score}", False, align=ALIGNMENT, font=FONT)

    def score(self):
        self.a_score += 1
        self.clear()
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)
