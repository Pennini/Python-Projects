from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.hideturtle()
        self.draw()

    def draw(self):
        self.clear()
        self.pensize(3)
        self.penup()
        self.goto(0, -295)
        self.pendown()
        self.setheading(90)
        for i in range(25):
            self.forward(12)
            self.penup()
            self.forward(12)
            self.pendown()
        self.penup()
        self.goto(-60, 200)
        self.write(f"{self.score_left}", move=False, font=("Courier", 60, "normal"))
        self.goto(15, 200)
        self.write(f"{self.score_right}", move=False, font=("Courier", 60, "normal"))

    def right_point(self):
        self.score_right += 1
        self.draw()

    def left_point(self):
        self.score_left += 1
        self.draw()
