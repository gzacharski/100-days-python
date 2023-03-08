from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.level_status = Turtle()
        self.level_status.hideturtle()
        self.game_over = Turtle()
        self.game_over.hideturtle()
        self.level_status.penup()
        self.level_status.shape("classic")
        self.score = 0
        self.level_status.goto(-280, 250)
        self.__refresh()

    def __refresh(self):
        self.level_status.clear()
        self.level_status.write(f"Level: {self.score}", False, "left", FONT)

    def increment_score(self):
        self.score += 1
        self.__refresh()

    def print_game_over(self):
        self.game_over.penup()
        self.game_over.write("Game over", False, "center", FONT)
