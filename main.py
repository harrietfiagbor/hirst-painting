import turtle
import random

# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

turtle.colormode(255)
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165),
              (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

hirst = turtle.Turtle()
hirst.speed("fastest")
hirst.penup()
hirst.hideturtle()
hirst.setpos(-700, -350)


def change_direction():
    if hirst.heading() == 0.0:
        for n in range(2):
            hirst.left(90)
            hirst.forward(50)
    elif hirst.heading() == 180:
        for n in range(2):
            hirst.left(270)
            hirst.forward(50)


loop_through = 20
for i in range(loop_through):
    for j in range(28):
        hirst.dot(20, random.choice(color_list))
        hirst.forward(50)
    change_direction()

screen = turtle.Screen()
screen.exitonclick()
