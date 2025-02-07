from turtle import Screen
from paddle import Paddle

HEIGHT = 600
WIDTH = 800
BACKGROUND_COLOR = "black"

screen = Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

r_paddle = Paddle(WIDTH/2 - 30, 0)
l_paddle = Paddle(-WIDTH/2 + 20, 0)

screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

screen.onkey(fun=l_paddle.go_up, key="w".lower())
screen.onkey(fun=l_paddle.go_down, key="s".lower())

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()
