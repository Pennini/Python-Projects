from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.create_paddle(location)

    def create_paddle(self, location):
        self.color("white")
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(location)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
