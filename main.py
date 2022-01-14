from turtle import Screen
from create_paddle import Paddle
from create_ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((340, 0))
l_paddle = Paddle((-340, 0))
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()
score = ScoreBoard()

is_on = True

while is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # detect when paddle misses
    if ball.xcor() > 380:
        ball.reset()
        score.calc_l_score()

    # detect when paddle misses
    if ball.xcor() < -380:
        ball.reset()
        score.calc_r_score()

screen.exitonclick()
