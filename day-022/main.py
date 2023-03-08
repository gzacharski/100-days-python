import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle(xcor=350, ycor=0)
paddle_left = Paddle(xcor=-350, ycor=0)

the_ball = Ball()
scoreboard = Scoreboard()

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

    # Detect collision with wall
    if the_ball.ycor() > 290 or the_ball.ycor() < -290:
        the_ball.bounce_y()

    # Detect collision with r_paddle
    if the_ball.distance(paddle_right) < 50 and the_ball.xcor() > 330 or the_ball.distance(
            paddle_left) < 50 and the_ball.xcor() < -330:
        the_ball.bounce_x()
        the_ball.increase_speed()

    if the_ball.xcor() < -380:
        the_ball.reset()
        scoreboard.score_right()

    if 380 < the_ball.xcor():
        the_ball.reset()
        scoreboard.score_left()

screen.exitonclick()
