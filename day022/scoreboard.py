from turtle import Turtle

ALIGNMENT = "center"
FONT= ("Helvetica", 30)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.write(f"{self.l_score}         {self.r_score}",align=ALIGNMENT, font=FONT)

    def r_score_increase(self):
        self.r_score += 1
        self.clear()
        self.write(f"{self.l_score}         {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_score_increase(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.l_score}         {self.r_score}", align=ALIGNMENT, font=FONT)
