from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.speed(0)
        self.goto(0, 275)
        self.initialize_score()
        self.track_score()

    def initialize_score(self):
        with open("high_score.txt") as file:
            self.high_score = int(file.read())

    def track_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score    
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.track_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)