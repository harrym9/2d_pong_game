import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

HEIGHT = 600
WIDTH = 800
BACKGROUND_COLOR = "black"

screen = Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

r_paddle = Paddle((WIDTH / 2 - 30, 0))
l_paddle = Paddle((-WIDTH / 2 + 20, 0))

ball = Ball()

score = ScoreBoard()

screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

screen.onkey(fun=l_paddle.go_up, key="w".lower())
screen.onkey(fun=l_paddle.go_down, key="s".lower())

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collisions with top and bottom walls
    if ball.ycor() >= ((HEIGHT / 2) - 20) or ball.ycor() <= -((HEIGHT / 2) - 20):
        ball.bounce_y()

    # Detect collisions with left and right paddle's
    if ball.xcor() >= ((WIDTH / 2) - 50) and ball.distance(r_paddle) < 50 or ball.xcor() <= -(
            (WIDTH / 2) - 40) and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detect when paddle's misses the ball
    if ball.xcor() >= 400:
        ball.restart()
        score.l_point()


    elif ball.xcor() <= -400:
        ball.restart()
        score.r_point()

screen.exitonclick()
