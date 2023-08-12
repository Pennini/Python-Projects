from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
colors = ["red", "green", "yellow", "blue", "purple", "orange"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? (red, green, yellow, blue, purple or orange): ")


while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? (red, green, yellow, blue, purple or orange): ")
turtles = []


def set_finish_line():
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.goto(230, 125)
    line.right(90)
    line.pendown()
    line.forward(250)


def set_race():
    y = 75
    set_finish_line()
    for turt in range(0, 6):
        turtle = Turtle()
        turtle.shape('turtle')
        turtle.color(colors[turt])
        turtle.penup()
        turtle.goto(-225, y)
        turtles.append(turtle)
        y -= 25


def race():
    is_on = True
    global winner
    while is_on:
        for turtle in range(0, 6):
            distance = random.randint(0, 10)
            turtles[turtle].forward(distance)
            if turtles[turtle].xcor() > 217: 
                winner = colors[turtle]
                is_on = False
                break


def compare():
    if winner == user_bet:
        print("You win, here is your payment!")
    else:
        print(f"You lose. The winner was {winner}")


set_race()
race()
compare()

screen.exitonclick()
    