from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.setx(0)
        self.sety(0)
        self.dot(size=20)
        self.penup()
        self.color("white")
        self.x_move = 1
        self.y_move = 1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1
