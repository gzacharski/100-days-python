import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle(xcor=350, ycor=0)
paddle_left = Paddle(xcor=-350, ycor=0)

the_ball = Ball()

screen.listen()
screen.onkeypress(paddle_right.move_up, "Up")
screen.onkeypress(paddle_right.move_down, "Down")

screen.onkeypress(paddle_left.move_up, "w")
screen.onkeypress(paddle_left.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    the_ball.move()

screen.exitonclick()