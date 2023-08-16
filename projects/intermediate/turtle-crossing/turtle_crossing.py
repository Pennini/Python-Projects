import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
turtle = Player()
score = Scoreboard()

screen.listen()

screen.onkeypress(key="Up", fun=turtle.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if turtle.win():
        car.update_level()
        score.update_score()
        turtle.start()