from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SNAKE_SPEED = 1
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            s = Turtle(shape='square')
            s.color('white')
            s.penup()
            s.speed(SNAKE_SPEED)
            s.goto(position)
            self.snakes.append(s)

    def extend(self):
        s = self.snakes[len(self.snakes) - 1].clone()
        s.backward(20)
        self.snakes.append(s)

    def reset(self):
        for snake in self.snakes:
            snake.hideturtle()
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            cor = self.snakes[snake_num - 1].pos()
            self.snakes[snake_num].goto(cor)
        self.snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

