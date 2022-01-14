from turtle import Turtle

Align = "LEFT"
Font = ('Arial', 45, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-280, 230)
        self.write(arg=self.l_score, move=False, align=Align, font=Font)
        self.goto(250, 230)
        self.write(arg=self.r_score, move=False, align=Align, font=Font)

    def calc_l_score(self):
        self.l_score += 1
        self.update()

    def calc_r_score(self):
        self.r_score += 1
        self.update()
