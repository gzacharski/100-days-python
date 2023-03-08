from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.setx(0)
        self.sety(0)
        self.dot(size=20)
        self.penup()
        self.color("white")

    def move(self):
        x = self.xcor() + 1
        y = self.ycor() + 1
        self.goto(x, y)
