from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    level = 1

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.write(f"Level: {self.level}", align="center", font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)
