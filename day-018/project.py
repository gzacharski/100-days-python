import colorgram
from turtle import Turtle, Screen
import random


def extract_colours():
    rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        r, g, b = color.rgb
        dot_color = float(r / 255), float(g / 255), float(b / 255)
        rgb_colors.append(dot_color)
    return rgb_colors


class Painting:
    def __init__(self):
        self.colours = extract_colours()
        self.the_turtle = Turtle()
        self.the_turtle.hideturtle()
        self.the_turtle.speed("fastest")

    def center_the_painting(self):
        self.the_turtle.penup()
        self.the_turtle.back(250)
        self.the_turtle.left(90)
        self.the_turtle.back(250)
        self.the_turtle.right(90)
        self.the_turtle.pendown()

    def __draw_dot(self):
        the_color = random.choice(self.colours)
        self.the_turtle.dot(20, the_color)
        self.the_turtle.penup()
        self.the_turtle.forward(50)
        self.the_turtle.pendown()

    def __move_to_the_next_line(self):
        self.the_turtle.penup()
        self.the_turtle.back(500)
        self.the_turtle.left(90)
        self.the_turtle.forward(50)
        self.the_turtle.right(90)
        self.the_turtle.pendown()

    def draw_the_painting(self):
        for _ in range(10):
            for _ in range(10):
                self.__draw_dot()
            self.__move_to_the_next_line()


painting = Painting()
painting.center_the_painting()
painting.draw_the_painting()

screen = Screen()
screen.exitonclick()
