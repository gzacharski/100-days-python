from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.setx(300 - STARTING_MOVE_DISTANCE)
        self.sety(random.randint(-250, 250))
        self.left(180)
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move(self, speed_factor=1):
        self.forward(MOVE_INCREMENT * speed_factor)

    def detect_collision(self, player):
        return self.distance(player) < 20


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed_factor = 1
        self.generate_new_cars()

    def generate_new_cars(self):
        for _ in range(random.randint(0, 3)):
            self.cars.append(Car())

    def move_cars(self):
        for car in self.cars:
            car.move(self.speed_factor)

    def detect_collision(self, player):
        detected_collision = False
        for car in self.cars:
            if car.detect_collision(player):
                detected_collision = True
                break
        return detected_collision

    def increment_speed(self):
        self.speed_factor += 0.25
