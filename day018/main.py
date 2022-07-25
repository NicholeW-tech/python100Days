import turtle as t
import random


# import colorgram
#
# import colorgram.colorgram
#
# another way to extract colors from images
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, b, g)
#     rgb_colors.append(new_color)

color_list = [(235, 250, 246), (251, 246, 241), (243, 74, 235), (211, 93, 158), (186, 69, 12), (112, 208, 179), (25, 168, 116), (173, 31, 171), (219, 166, 129), (161, 35, 79), (129, 146, 185), (9, 76, 32), (222, 105, 62), (235, 42, 73), (180, 94, 45), (30, 81, 136), (236, 193, 164), (78, 63, 12), (12, 33, 54), (234, 7, 227), (26, 209, 165), (16, 132, 43), (58, 96, 166), (134, 229, 214), (10, 63, 101), (133, 20, 34), (91, 11, 27), (159, 188, 211)]

tim = t.Turtle
t.colormode(255)
t.speed("fastest")
t.hideturtle()

def random_color():
    color = random.choice(color_list)
    return color




def make_painting():
    t.penup()
    t.setpos(-200, -200)
    t.pendown()
    for i in range(10):
        for _ in range(10):
            t.color(random_color())
            t.dot(20)
            t.penup()
            t.fd(50)
            t.pendown()
        t.penup()
        t.setheading(90)
        t.forward(20)
        t.setheading(180)
        t.forward(500)
        t.setheading(90)
        t.forward(20)
        t.setheading(0.0)




# t.dot(20, "blue")
# t.penup()
# t.fd(50)

make_painting()


my_screen = t.Screen()
my_screen.exitonclick()
