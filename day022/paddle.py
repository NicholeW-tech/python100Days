from turtle import Turtle

DOWN = 270
UP = 90
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(position)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


