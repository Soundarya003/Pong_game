from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_forward = 10
        self.y_forward = 10
        self.move_speed = 0.07

    def move_ball(self):
        new_x = self.xcor() + self.x_forward
        new_y = self.ycor() + self.y_forward
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_forward *= -1

    def x_bounce(self):
        self.x_forward *= -1

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.07
        self.x_bounce()

