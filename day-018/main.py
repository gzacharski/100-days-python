from turtle import Turtle as MyTurtle, Screen as MyScreen


class TimmyTheTurtle:
    def __init__(self):
        self.turtle = MyTurtle()
        self.turtle.shape("turtle")
        self.turtle.color("gray")

    def draw_a_square(self):
        for _ in range(4):
            self.turtle.forward(100)
            self.turtle.right(90)


timmy_the_turtle = TimmyTheTurtle()
timmy_the_turtle.draw_a_square()

screen = MyScreen()
screen.exitonclick()
