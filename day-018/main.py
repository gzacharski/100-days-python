from turtle import Turtle as MyTurtle, Screen as MyScreen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


class TimmyTheTurtle:
    def __init__(self):
        self.turtle = MyTurtle()
        self.turtle.shape("turtle")
        self.turtle.color("gray")

    def draw_a_square(self):
        for _ in range(4):
            self.turtle.forward(100)
            self.turtle.right(90)

    def draw_a_dashed_line(self, distance):
        for _ in range(int(distance / 10)):
            self.turtle.penup()
            self.turtle.forward(10)
            self.turtle.pendown()
            self.turtle.forward(10)

    def draw_different_shapes(self):
        for i in range(3, 9):
            colour = random.choice(colours)
            for _ in range(i):
                self.turtle.forward(100)
                self.turtle.right(360 / i)
                self.turtle.color(colour)

    def draw_random_walk(self, iterations):
        angles = [0, 90, 180, 270]
        self.turtle.speed("fastest")
        self.turtle.pensize(10)
        for _ in range(iterations):
            angle = random.choice(angles)
            colour = random.choice(colours)
            self.turtle.color(colour)
            self.turtle.right(angle)
            self.turtle.forward(100)


timmy_the_turtle = TimmyTheTurtle()
timmy_the_turtle.draw_random_walk(200)

screen = MyScreen()
screen.exitonclick()
