# import colorgram

# rgb_painting = colorgram.extract('hirst_painting.jpg', 160)
# color_palette = []

# for color in rgb_painting:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_palette.append((r, g, b))
from turtle import Turtle, Screen
import random

colors = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()
tim.setposition(-225, -225)


def line():
    tim.dot(20, random.choice(colors))
    tim.forward(50)

for dot_count in range(1, 101):
    line()
    if dot_count % 10 == 0:
        tim.backward(500)
        tim.left(90)
        tim.forward(50)
        tim.right(90)


screen.exitonclick()