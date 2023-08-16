from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.level = 0
        self.make_car()


    def make_car(self):
        self.car = Turtle(shape="square")
        self.car.color(random.choice(COLORS))
        self.car.shapesize(stretch_len=2)
        self.car.setheading(180)
        self.car.penup()
        self.car.goto(300, random.randint(-280, 280))
        move = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * self.level
        self.car.forward(move)

    def update_level(self):
        self.level += 1
