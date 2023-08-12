from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

screen.colormode(255)
tim.speed(0)

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color = (r, g, b)
    return color

def draw_shapes():
    n = 3
    tim.penup()
    tim.goto(-50, 150)
    tim.pendown()
    while n <= 10:
        angle = 360 / n
        tim.pencolor(random_color())
        for _ in range(n):
            tim.forward(100)
            tim.right(angle)
        n += 1

def random_walk():
    directions = [0, 90, 180, 270]
    tim.pensize(15)
    tim.hideturtle()
    for _ in range(200):
        tim.pencolor(random_color())

        tim.forward(30)
        tim.setheading(random.choice(directions))

def draw_spirograph(size_gap):
    tim.hideturtle()
    tim.pensize(2)
    for _ in range(int(360 / size_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_gap)



def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_anti_clock():
    tim.left(10)

def move_clockwise():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def make_dot():
    tim.dot(5)

 

# screen.listen()
# screen.onkey(key='w', fun=move_forward)
# screen.onkey(key='s', fun=move_backward)
# screen.onkey(key='a', fun=move_anti_clock)
# screen.onkey(key='d', fun=move_clockwise)
# screen.onkey(key='c', fun=clear_screen)
# screen.onkey(key='space', fun=make_dot)
# screen.onkey(key='z', fun=tim.pendown)
# screen.onkey(key='x', fun=tim.penup)

def move(steps, direction):
    for _ in range(steps):
        if direction == "forward":
            tim.forward(10)
        elif direction == "backward":
            tim.backward(10)
        elif direction == "left":
            tim.left(10)
        elif direction == "right":
            tim.right(10)

def make_degree():
    move(10, "forward")
    move(20, "backward")
    move(10, "forward")
    move(9, "left")
    move(15, "forward")
    move(13, "backward")
    move(9, "right")
    move(2, "forward")
    move(9, "right")
    move(2, "forward")
    tim.penup()
    move(9, "right")
    move(1, "forward")
    move(9, "right")
    move(1, "forward")
    make_dot(tim)
    tim.hideturtle()

# screen.setup(width=500, height=400)
# colors = ["red", "green", "yellow", "blue", "purple", "orange"]
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? (red, green, yellow, blue, purple or orange): ")
# while user_bet not in colors:
#     user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? (red, green, yellow, blue, purple or orange): ")
# turtles = []
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
    """_summary_
    """    for turt in range(0, 6):
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


screen.exitonclick()