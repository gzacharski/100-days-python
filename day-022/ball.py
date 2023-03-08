from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.setx(0)
        self.sety(0)
        self.dot(size=20)
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.speed_factor = 0.1

    def move(self):
        x = self.xcor() + self.x_move * self.speed_factor
        y = self.ycor() + self.y_move * self.speed_factor
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.speed_factor = 0.1

    def increase_speed(self):
        self.speed_factor += 0.05
