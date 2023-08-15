from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed(0)
        self.penup()
        self.distance_x = 10
        self.distance_y = 10

    def move(self):
        new_x = self.xcor() + self.distance_x
        new_y = self.ycor() + self.distance_y
        self.goto(new_x, new_y)

    def bounce(self):
        self.distance_y *= -1

    def pong(self):
        self.distance_x *= -1
