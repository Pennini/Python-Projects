from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detectar colisão com a comida
    if snake.head.distance(food) < 17:
        food.refresh()
        score.score += 1
        score.track_score()
        snake.extend()

    # Detectar colisão com a parede
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        is_game_on = False

    # Detectar colisão com com  a cauda
    for s in snake.snakes[1:]:
        if snake.head.distance(s) < 10:
            is_game_on = False

score.game_over()
screen.exitonclick()