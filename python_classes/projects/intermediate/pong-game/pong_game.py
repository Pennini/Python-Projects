from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()

screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


x = 0.1
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(x)
    ball.move()

    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce()
    if (
        ball.distance(l_paddle) < 50
        and ball.xcor() < -320
        or ball.distance(r_paddle) < 50
        and ball.xcor() > 320
    ):
        ball.pong()
        x *= 0.9
    if ball.xcor() > 360:
        score.left_point()
        ball.pong()
        ball.goto(0, 0)
        x = 0.1
    elif ball.xcor() < -360:
        score.right_point()
        ball.pong()
        ball.goto(0, 0)
        x = 0.1

screen.exitonclick()
