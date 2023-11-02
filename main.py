from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

TOP_SCREEN = 300
BOTTOM_SCREEN = -300

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
ball_x = 0
ball_y = 0


while game_is_on:
    time.sleep(0.1)
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    
    ball.move_ball()




screen.exitonclick()