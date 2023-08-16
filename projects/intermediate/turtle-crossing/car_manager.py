from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.level = 0
        self.cars = []
        self.make_car()

    def make_car(self):
        randomness = random.randint(1, 5)
        if randomness == 1:
            c = Turtle(shape='square')
            c.color(random.choice(COLORS))
            c.shapesize(stretch_len=2)
            c.penup()
            c.goto(320, random.randint(-250, 250))
            self.cars.append(c)
        
    def move(self):
        for car in range(len(self.cars) - 1):
            move = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * self.level
            self.cars[car].backward(move)

    def update_level(self):
        self.level += 1
        for car in self.cars:
            car.hideturtle()
        self.cars = []
