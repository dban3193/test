# import colorgram
# colors = colorgram.extract("image.jpg", 15)
#above image was present under same root in project, and 15 is no of colors
# get_shade = []
# rgb = []
# for i in range(len(colors)):
#     get_shade = colors[i].rgb
#     r = get_shade.r
#     b = get_shade.b
#     g = get_shade.g
#     color_tuple = (r, g, b)
#     rgb.append(color_tuple)
#
# print(rgb)
#Above logic was used to get the color_list below.


from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)

color_list = [(228, 225, 222), (231, 206, 83), (229, 147, 85), (217, 227, 219), (119, 166, 186), (160, 13, 19),
              (232, 221, 226), (30, 110, 159), (235, 81, 44), (215, 222, 228), (5, 99, 37), (176, 19, 14),
              (187, 187, 25), (121, 177, 144), (207, 62, 22)]

# TODO 1: Create a dot painting by Hirst

timmy = Turtle()
# to remove line trace
timmy.penup()
# to remove turtle icon
timmy.hideturtle()
timmy.speed("fastest")

# to go from 0 to 300 with pace = 30
for upward in range(0, 300, 30):
    # always start from (-180,upward) position
    timmy.goto(-180, upward)
    # for horizontal printing 10 dots
    for pace in range(10):
        # create a dot of size 10 and a random color from the lot
        timmy.dot(10, random.choice(color_list))
        # pace forward by 30 after every dot
        timmy.forward(30)

screen = Screen()
screen.exitonclick()
