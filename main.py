from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time

# Screen
screen = Screen()
screen.bgcolor("black")
screen.title("Py-Pong")
screen.setup(800, 600)
screen.listen()

screen.tracer(0)


line = Line()
line.drawing()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

scoreboard = Scoreboard()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

playing = True
while playing:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 or ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        screen.update()

    if ball.xcor() < -350:
        ball.center_reset()
        scoreboard.r_point()

    if ball.xcor() > 350:
        ball.center_reset()
        scoreboard.l_point()

screen.exitonclick()
