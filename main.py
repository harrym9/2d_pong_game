from turtle import Turtle, Screen

HEIGHT = 600
WIDTH = 800
BACKGROUND_COLOR = "black"

screen = Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong Game")
screen.listen()
screen.tracer(0)


def up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


paddle = Turtle()
paddle.color("white")
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(x=(WIDTH // 2) - 30, y=0)

screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()
