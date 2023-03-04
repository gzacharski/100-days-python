from turtle import Turtle, Screen


def draw_a_square():
    for _ in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("gray")

draw_a_square()

screen = Screen()
screen.exitonclick()
