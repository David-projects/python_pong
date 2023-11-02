from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from playerscore import PlayerScore

TOP_SCREEN = 300
BOTTOM_SCREEN = -300

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)
r_paddle = Paddle((350, 0))
r_score = PlayerScore((50, 260))
l_paddle = Paddle((-350, 0))
l_score = PlayerScore((-50, 260))
ball = Ball()
game_is_on = True


def endgame():
    game_is_on = False


screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(endgame, "e")

ball_x = 0
ball_y = 0

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with r paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect ball miss the paddle
    if ball.xcor() > 400:
        l_score.update_score()
        ball.restart()
    if ball.xcor() < -400:
        r_score.update_score()
        ball.restart()

screen.exitonclick()
