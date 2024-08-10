# import colorgram
# colors = colorgram.extract('img.png', 20)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     rgb_colors.append((r, g, b))

import turtle
from random import choice
from turtle import Turtle as T, Screen as S

color_list = [(239, 229, 212), (63, 28, 7), (87, 95, 112), (243, 217, 234), (166, 83, 30), (219, 159, 82),
              (211, 224, 233), (140, 156, 180), (88, 108, 96), (211, 161, 13), (225, 236, 230), (236, 217, 81),
              (206, 6, 24), (18, 20, 53), (142, 160, 151), (22, 38, 27), (240, 65, 43), (79, 107, 202), (33, 45, 132),
              (182, 15, 6)]

tim = T()
tim.pensize(20)
turtle.colormode(255)
tim.speed("fastest")
tim.hideturtle()

def make_the_dots():
    for i in range(15):
        r_color = choice(color_list)
        tim.color(r_color)
        tim.pendown()
        tim.forward(5)
        tim.penup()
        tim.forward(50)
        tim.pendown()

def get_in_pos():
    tim.penup()
    tim.left(180)
    tim.forward(400)
    tim.left(90)
    tim.forward(350)
    tim.left(90)

def one_step_up():
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(825)
    tim.right(180)


get_in_pos()

for i in range(15):
    make_the_dots()
    one_step_up()





screen = S()
screen.exitonclick()
