from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.back(10)


def rotate_counter_clockwise():
    turtle.left(10)


def rotate_clockwise():
    turtle.right(10)


def clear_painting():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=rotate_counter_clockwise)
screen.onkeypress(key="d", fun=rotate_clockwise)
screen.onkeypress(key="c", fun=clear_painting)
screen.exitonclick()
