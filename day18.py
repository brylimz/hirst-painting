import random
import turtle as t
from random import Random
from turtle import Turtle, Screen
tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

# tim.shape("turtle")
# tim.color("blue", "black")
# colours = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 98, 180, 270]
#

# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#

#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)
#
#
#
#
#
#
#
#

screen = Screen()

screen.exitonclick()
