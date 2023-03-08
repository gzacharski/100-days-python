import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.move, "Up")

game_is_on = True
iterator = 0
while game_is_on:
    iterator += 1
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    if iterator % 4 == 0:
        car_manager.generate_new_cars()

    if car_manager.detect_collision(player):
        scoreboard.print_game_over()
        game_is_on = False

    if player.reach_finish_line():
        scoreboard.increment_score()
        player.reset()
        car_manager.increment_speed()

screen.exitonclick()
